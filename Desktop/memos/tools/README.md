# Memo Tools

These scripts turn local voice memos into transcript artifacts and meeting notes.

## Requirements

- `ffmpeg`
- `ffprobe`
- `curl`
- `jq`
- `claude`
- local `voxtype` HTTP transcription service

Default assumptions:

- transcription endpoint: `http://127.0.0.1:8427`
- output root: `$HOME/Nextcloud/plasma/DOCUMENTS/MEETINGS`
- note language: English
- meeting folder selection prefers an existing archive folder when the recording date, filename, and prior metadata strongly match

## Transcribe

```bash
tools/transcribe-memo 2026-03-24_computor_jf.qta
```

Useful overrides:

```bash
tools/transcribe-memo \
  --meeting-name computor_jf \
  --language auto \
  --multilingual \
  --base-url http://127.0.0.1:8427 \
  2026-03-24_computor_jf.qta
```

If a matching meeting folder already exists in the archive, the scripts reuse it instead of creating a second near-duplicate folder.

Artifacts written into the meeting folder:

- `metadata.json`
- `transcript.json`
- `transcript.txt`
- `transcript.srt`
- `transcript.vtt`
- `transcript.tsv`

## Generate Notes

```bash
tools/generate-meeting-notes \
  --multilingual \
  --extra-prompt "Focus on follow-up tasks and paper-writing decisions." \
  /Users/ert/Nextcloud/plasma/DOCUMENTS/MEETINGS/2026-03-23_computor_jf
```

Outputs:

- `MEETING_NOTES.md`
- `TODO.md`

## One Shot

```bash
tools/process-memo \
  --language auto \
  --multilingual \
  --notes-language en \
  2026-03-24_computor_jf.qta
```
