#!/usr/bin/env bash

set -euo pipefail

default_output_root() {
    printf '%s\n' "${MEETING_OUTPUT_ROOT:-$HOME/Nextcloud/plasma/DOCUMENTS/MEETINGS}"
}

default_whisper_base_url() {
    printf '%s\n' "${WHISPER_BASE_URL:-${OPENAI_BASE_URL:-http://127.0.0.1:8427}}"
}

default_whisper_model() {
    printf '%s\n' "${WHISPER_MODEL:-${OPENAI_MODEL:-whisper-1}}"
}

default_whisper_api_key() {
    printf '%s\n' "${WHISPER_API_KEY:-${OPENAI_API_KEY:-}}"
}

default_meeting_timezone() {
    printf '%s\n' "${MEETING_TIMEZONE:-Europe/Vienna}"
}

die() {
    printf 'Error: %s\n' "$*" >&2
    exit 1
}

require_cmd() {
    command -v "$1" >/dev/null 2>&1 || die "missing required command: $1"
}

abs_path() {
    local target="$1"
    if [[ -d "$target" ]]; then
        (cd "$target" && pwd)
    else
        local dir base
        dir="$(dirname "$target")"
        base="$(basename "$target")"
        (cd "$dir" && printf '%s/%s\n' "$(pwd)" "$base")
    fi
}

slugify() {
    printf '%s' "$1" \
        | tr '[:upper:]' '[:lower:]' \
        | sed -E 's/\.[^.]+$//; s/[^a-z0-9]+/_/g; s/^_+//; s/_+$//; s/__+/_/g'
}

default_meeting_slug_source() {
    local stem="$1"
    printf '%s' "$stem" | sed -E 's/^[0-9]{4}[-_][0-9]{2}[-_][0-9]{2}[-_]?//'
}

strip_meeting_date_prefix() {
    local name="$1"
    printf '%s' "$name" | sed -E 's/^[0-9]{4}([_-][0-9]{2}){0,2}[_-]?//'
}

meeting_name_date_prefix() {
    local name="$1"
    local prefix

    prefix="$(printf '%s' "$name" | sed -En 's/^([0-9]{4}([_-][0-9]{2}){0,2}).*/\1/p')"
    printf '%s\n' "${prefix//_/-}"
}

slug_tokens() {
    printf '%s\n' "$1" \
        | tr '_' '\n' \
        | awk 'length($0) >= 2 && $0 !~ /^[0-9]+$/ { print }' \
        | sort -u
}

token_overlap_score() {
    local left="$1"
    local right="$2"

    comm -12 <(slug_tokens "$left") <(slug_tokens "$right") | awk 'END { print NR + 0 }'
}

resolve_meeting_dir() {
    local output_root="$1"
    local recorded_date="$2"
    local stem="$3"
    local meeting_name="${4:-}"
    local audio_basename="${5:-}"
    local slug_source desired_slug exact_dir
    local best_dir="" best_reason="" best_score=0
    local candidate_dir candidate_base candidate_slug candidate_date
    local metadata_file metadata_source_name metadata_source_slug
    local overlap score

    slug_source="${meeting_name:-$(default_meeting_slug_source "$stem")}"
    if [[ -z "$slug_source" ]]; then
        slug_source="$stem"
    fi
    desired_slug="$(slugify "$slug_source")"
    exact_dir="$output_root/${recorded_date}_${desired_slug}"

    if [[ -e "$exact_dir" ]]; then
        printf '%s\t%s\t%s\n' "$exact_dir" "exact_path" "$desired_slug"
        return 0
    fi

    shopt -s nullglob
    for candidate_dir in "$output_root"/*; do
        [[ -d "$candidate_dir" ]] || continue

        candidate_base="$(basename "$candidate_dir")"
        candidate_slug="$(slugify "$(strip_meeting_date_prefix "$candidate_base")")"
        candidate_date="$(meeting_name_date_prefix "$candidate_base")"
        metadata_file="$candidate_dir/metadata.json"
        score=0

        if [[ -n "$candidate_slug" && "$candidate_slug" == "$desired_slug" ]]; then
            score=$((score + 120))
        fi

        overlap="$(token_overlap_score "$desired_slug" "$candidate_slug")"
        score=$((score + overlap * 25))

        if [[ -n "$desired_slug" && -n "$candidate_slug" ]]; then
            if [[ "$candidate_slug" == *"$desired_slug"* || "$desired_slug" == *"$candidate_slug"* ]]; then
                score=$((score + 15))
            fi
        fi

        if [[ -n "$candidate_date" && "$candidate_date" == "$recorded_date" ]]; then
            score=$((score + 80))
        elif [[ -n "$candidate_date" && "${candidate_date:0:7}" == "${recorded_date:0:7}" ]]; then
            score=$((score + 20))
        fi

        if [[ -f "$metadata_file" ]]; then
            metadata_source_name="$(jq -r '.source_file_name // empty' "$metadata_file" 2>/dev/null || true)"
            metadata_source_slug="$(slugify "${metadata_source_name%.*}")"
            if [[ -n "$audio_basename" && "$metadata_source_name" == "$audio_basename" ]]; then
                score=$((score + 240))
            fi
            if [[ -n "$metadata_source_slug" && "$metadata_source_slug" == "$(slugify "${audio_basename%.*}")" ]]; then
                score=$((score + 90))
            fi
        fi

        if ((score > best_score)); then
            best_score="$score"
            best_dir="$candidate_dir"
            best_reason="archive_match"
        fi
    done
    shopt -u nullglob

    if ((best_score >= 140)); then
        printf '%s\t%s\t%s\n' "$best_dir" "$best_reason" "$desired_slug"
    else
        printf '%s\t%s\t%s\n' "$exact_dir" "new_path" "$desired_slug"
    fi
}

default_transcription_prompt() {
    local multilingual="${1:-0}"

    if [[ "$multilingual" == "1" ]]; then
        printf '%s' 'Meeting recording. The conversation may switch between German and English. Transcribe as literally as possible and preserve names, acronyms, technical terms, code identifiers, and mixed-language speech carefully. Relevant terms may include computor, Netidee, fusion plasma physics, university teaching, academic administration, HPC, programming, Docker, VS Code, Playwright, Ollama, MLX LM, Qwen, GPT OSS, Linux, and Windows.'
    else
        printf '%s' 'Meeting recording. Transcribe as literally as possible and preserve names, acronyms, technical terms, code identifiers, and domain-specific speech carefully. Relevant terms may include computor, Netidee, fusion plasma physics, university teaching, academic administration, HPC, programming, Docker, VS Code, Playwright, Ollama, MLX LM, Qwen, GPT OSS, Linux, and Windows.'
    fi
}

json_string_file() {
    jq -Rs . < "$1"
}

cleanup_transcript_artifacts() {
    local meeting_dir="$1"

    rm -f \
        "$meeting_dir/transcript.json" \
        "$meeting_dir/transcript.txt" \
        "$meeting_dir/transcript.srt" \
        "$meeting_dir/transcript.vtt" \
        "$meeting_dir/transcript.tsv" \
        "$meeting_dir/metadata.json"
}

pick_recorded_at() {
    local ffprobe_json="$1"
    local source_file="$2"
    local ffprobe_creation mdls_creation stat_creation

    ffprobe_creation="$(jq -r '
        .format.tags.creation_time
        // ([.streams[].tags.creation_time?] | map(select(. != null)) | first)
        // empty
    ' "$ffprobe_json")"

    mdls_creation="$(mdls -raw -name kMDItemContentCreationDate "$source_file" 2>/dev/null || true)"
    if [[ "$mdls_creation" == "(null)" ]]; then
        mdls_creation=""
    fi

    stat_creation="$(stat -f '%SB' -t '%Y-%m-%d %H:%M:%S %z' "$source_file" 2>/dev/null || true)"

    if [[ -n "$ffprobe_creation" ]]; then
        printf '%s\t%s\n' "$ffprobe_creation" "ffprobe.format.tags.creation_time"
    elif [[ -n "$mdls_creation" ]]; then
        printf '%s\t%s\n' "$mdls_creation" "mdls.kMDItemContentCreationDate"
    else
        printf '%s\t%s\n' "$stat_creation" "stat.birth_time"
    fi
}

recorded_date_part() {
    local recorded_at="$1"
    local date_part

    date_part="$(printf '%s' "$recorded_at" | sed -E 's/^([0-9]{4}-[0-9]{2}-[0-9]{2}).*/\1/')"
    if [[ "$date_part" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
        printf '%s\n' "$date_part"
    else
        date '+%Y-%m-%d'
    fi
}

recorded_at_local() {
    local recorded_at="$1"
    local clean
    local meeting_timezone

    if [[ "$recorded_at" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}T.*Z$ ]]; then
        clean="${recorded_at%%.*}"
        clean="${clean%Z}"
        meeting_timezone="$(default_meeting_timezone)"
        TZ="$meeting_timezone" date -j -f '%Y-%m-%dT%H:%M:%S %z' \
            "$clean +0000" '+%Y-%m-%d %H:%M:%S %z'
    else
        printf '%s\n' "$recorded_at"
    fi
}

format_timestamp() {
    local seconds="$1"
    local separator="$2"

    awk -v total="$seconds" -v sep="$separator" '
        BEGIN {
            if (total == "" || total == "null") {
                total = 0
            }
            ms = int((total + 0.0005) * 1000)
            h = int(ms / 3600000)
            ms %= 3600000
            m = int(ms / 60000)
            ms %= 60000
            s = int(ms / 1000)
            ms %= 1000
            printf "%02d:%02d:%02d%s%03d", h, m, s, sep, ms
        }
    '
}

write_segment_formats() {
    local transcript_json="$1"
    local srt_file="$2"
    local vtt_file="$3"
    local tsv_file="$4"
    local segment index start end text

    : > "$srt_file"
    printf 'WEBVTT\n\n' > "$vtt_file"
    printf 'start\tend\ttext\n' > "$tsv_file"

    index=1
    while IFS= read -r segment; do
        start="$(printf '%s' "$segment" | base64 --decode | jq -r '.start')"
        end="$(printf '%s' "$segment" | base64 --decode | jq -r '.end')"
        text="$(printf '%s' "$segment" | base64 --decode | jq -r '.text')"

        printf '%s\n%s --> %s\n%s\n\n' \
            "$index" \
            "$(format_timestamp "$start" ',')" \
            "$(format_timestamp "$end" ',')" \
            "$text" >> "$srt_file"

        printf '%s --> %s\n%s\n\n' \
            "$(format_timestamp "$start" '.')" \
            "$(format_timestamp "$end" '.')" \
            "$text" >> "$vtt_file"

        printf '%s\t%s\t%s\n' \
            "$start" \
            "$end" \
            "$text" >> "$tsv_file"

        index=$((index + 1))
    done < <(jq -r '.segments[]? | @base64' "$transcript_json")
}
