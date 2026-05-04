"""Numerical helpers for the lecture 7 pendulum analysis scripts."""
import time

import numpy as np
from scipy.interpolate import CubicSpline, PchipInterpolator, interp1d
from scipy.optimize import curve_fit, fmin

from src.data_io import load_sine_params
from src.trajectory import exponential_decay, sine


def load_centered_x(csv_path):
    rows = np.loadtxt(csv_path, delimiter=",", skiprows=1)
    t, x = rows[:, 0], rows[:, 1]
    return centred_valid_trace(t, x)


def local_parabola_fit(t_all, x_all, half_width):
    t, x, t_peak = select_window_around_first_peak(t_all, x_all, half_width)
    coeffs = fit_via_normal_equations(design_matrix_quadratic(t), x)
    polyfit_coeffs = np.polyfit(t, x, deg=2)[::-1]
    return t, x, t_peak, coeffs, polyfit_coeffs


def fit_sine_with_stride(t, x, p0, stride=1):
    t_fit, x_fit = downsample(t, x, stride)
    popt, pcov = fit_sine(t_fit, x_fit, p0)
    parameter_errors = np.sqrt(np.diag(pcov))
    chi2 = float(np.sum((x_fit - sine(t_fit, popt[0], popt[1], popt[2])) ** 2))
    return t_fit, x_fit, popt, parameter_errors, chi2


def fit_sine_and_find_extrema(t, x, p0):
    popt = fit_curve(t, x, p0)
    half_period = np.pi / popt[1] if popt[1] != 0 else 1.0
    t_min, y_min = find_min(popt, t_seed=t[0] + half_period)
    t_max, y_max = find_max(popt, t_seed=t[0])
    return popt, t_min, y_min, t_max, y_max


def interpolation_results(t, x, t0, t1):
    t_seg, x_seg = segment(t, x, t0, t1)
    t_dense = np.linspace(t_seg[0], t_seg[-1], 500)
    return t_seg, x_seg, t_dense, interpolate_all(t_seg, x_seg, t_dense)


def fit_decay_both_ways(t, x, p0, min_fraction=0.15, repeat=50):
    t_peaks, amplitudes = peak_envelope_points(t, x, min_fraction=min_fraction)
    log_result, log_seconds = time_repeated(
        lambda: fit_log_envelope(t_peaks, amplitudes), repeat=repeat,
    )
    exp_result, exp_seconds = time_repeated(
        lambda: fit_exponential_envelope(t_peaks, amplitudes, p0), repeat=repeat,
    )
    log_amplitude, log_tau, log_line = log_result
    exp_amplitude, exp_tau = exp_result[0]
    return (
        t_peaks,
        amplitudes,
        log_amplitude,
        log_tau,
        log_line,
        log_seconds,
        exp_amplitude,
        exp_tau,
        exp_seconds,
    )


def default_sine_p0(t, x, csv_path=None):
    if csv_path is not None:
        params = load_sine_params(csv_path)
        if params is not None:
            return params
    return auto_p0(t, x)


def centred_valid_trace(t, x):
    valid = ~np.isnan(x)
    t = t[valid]
    x = x[valid]
    return t, x - np.nanmean(x)


def select_window_around_first_peak(t, x, half_width):
    centred = x - np.nanmean(x)
    i_peak = int(np.nanargmax(np.abs(centred)))
    t_peak = t[i_peak]
    mask = (t >= t_peak - half_width) & (t <= t_peak + half_width)
    return t[mask], x[mask], t_peak


def design_matrix_quadratic(t):
    return np.column_stack([np.ones_like(t), t, t ** 2])


def fit_via_normal_equations(A, y):
    return np.linalg.solve(A.T @ A, A.T @ y)


def centred_x(t, x):
    return x - np.nanmean(x)


def downsample(t, x, stride):
    stride = max(1, int(stride))
    return t[::stride], x[::stride]


def wrap_phase(phi):
    return (float(phi) + np.pi) % (2.0 * np.pi) - np.pi


def canonicalize_sine_params(params):
    amplitude, omega, phase = [float(v) for v in params]
    if omega < 0:
        omega = -omega
        phase = -phase
    if amplitude < 0:
        amplitude = -amplitude
        phase += np.pi
    return np.array([amplitude, omega, wrap_phase(phase)], dtype=float)


def auto_p0(t, x):
    amplitude = float(np.sqrt(2.0) * np.std(x))
    omega = estimate_omega_fft(t, x)
    if omega is None:
        duration = float(t[-1] - t[0]) if len(t) > 1 else 1.0
        omega = 2.0 * np.pi / duration
    phase = estimate_phase(t, x, omega)
    return [amplitude, float(omega), phase]


def estimate_omega_fft(t, x):
    if t.size < 8:
        return None
    dt = float(np.median(np.diff(t)))
    if not np.isfinite(dt) or dt <= 0:
        return None
    y = x - np.mean(x)
    freqs = np.fft.rfftfreq(y.size, d=dt)
    magnitudes = np.abs(np.fft.rfft(y))
    if freqs.size < 2:
        return None
    magnitudes[0] = 0.0
    idx = int(np.argmax(magnitudes))
    if idx <= 0 or freqs[idx] <= 0:
        return None
    return 2.0 * np.pi * float(freqs[idx])


def estimate_phase(t, x, omega):
    basis = np.column_stack([np.sin(omega * t), np.cos(omega * t)])
    result = np.linalg.lstsq(basis, x, rcond=None)
    coeffs = result[0]
    return float(np.arctan2(coeffs[1], coeffs[0]))


def fit_sine(t, x, p0):
    popt, pcov = curve_fit(sine, t, x, p0=p0, maxfev=10000)
    return canonicalize_sine_params(popt), pcov


def fit_curve(t, x, p0):
    popt, _ = curve_fit(sine, t, x, p0=p0, maxfev=10000)
    return canonicalize_sine_params(popt)


def fitted_value(t_scalar, popt):
    return sine(np.array([t_scalar]), popt[0], popt[1], popt[2])[0]


def find_min(popt, t_seed):
    t_min = float(fmin(lambda t: fitted_value(t[0], popt), [t_seed], disp=False)[0])
    return t_min, fitted_value(t_min, popt)


def find_max(popt, t_seed):
    t_max = float(fmin(lambda t: -fitted_value(t[0], popt), [t_seed], disp=False)[0])
    return t_max, fitted_value(t_max, popt)


def segment(t, x, t0, t1):
    if t1 < t0:
        t0, t1 = t1, t0
    mask = (t >= t0) & (t <= t1)
    return t[mask], x[mask]


def interpolate_all(t_data, x_data, t_dense):
    return {
        "nearest": interp1d(t_data, x_data, kind="nearest")(t_dense),
        "linear": interp1d(t_data, x_data)(t_dense),
        "pchip": PchipInterpolator(t_data, x_data)(t_dense),
        "cubic": CubicSpline(t_data, x_data)(t_dense),
    }


def peak_envelope_points(t, x, min_fraction=0.15):
    amplitude = np.abs(x)
    is_peak = (amplitude[1:-1] >= amplitude[:-2]) & (amplitude[1:-1] > amplitude[2:])
    indices = np.nonzero(is_peak)[0] + 1
    if indices.size == 0:
        indices = np.array([int(np.argmax(amplitude))])
    threshold = min_fraction * np.nanmax(amplitude)
    indices = indices[amplitude[indices] >= threshold]
    if indices.size < 2:
        largest = np.argsort(amplitude)[-2:]
        indices = np.sort(largest)
    return t[indices], amplitude[indices]


def fit_log_envelope(t_peaks, amplitudes):
    amplitudes = np.clip(amplitudes, 1e-12, None)
    slope, intercept = np.polyfit(t_peaks, np.log(amplitudes), deg=1)
    slope = min(slope, -1e-12)
    tau = -1.0 / slope
    return float(np.exp(intercept)), float(tau), np.array([slope, intercept])


def fit_exponential_envelope(t_peaks, amplitudes, p0):
    return curve_fit(exponential_decay, t_peaks, amplitudes, p0=p0, maxfev=10000)


def time_repeated(fn, repeat):
    start = time.perf_counter()
    result = None
    for _ in range(repeat):
        result = fn()
    return result, (time.perf_counter() - start) / repeat
