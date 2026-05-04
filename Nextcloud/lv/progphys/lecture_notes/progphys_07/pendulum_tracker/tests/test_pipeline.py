"""End-to-end: synthetic frames -> detection -> CSV -> reload -> fit -> recover."""
import math
import os
import tempfile

import numpy as np
from scipy.optimize import curve_fit

from pendulum_tracker.src.color_detection import detect_bright_centroid
from pendulum_tracker.src.data_io import save_track_csv
from pendulum_tracker.src.frame_source import synthetic_frames
from pendulum_tracker.src.trajectory import damped_sine


def test_pipeline_recovers_damped_sine_parameters():
    frame_size = (240, 320)
    centre_x = 160
    centre_y = 120
    truth = dict(amplitude=120.0, omega=2.0 * math.pi * 0.6, phase=0.3, tau=4.0)

    def trajectory(t):
        return centre_x + damped_sine(t, **truth), centre_y

    times, xs = [], []
    for t, frame in synthetic_frames(trajectory, fps=20, duration=8.0,
                                     frame_size=frame_size, noise_sigma=2.0):
        cxy = detect_bright_centroid(frame, threshold=200)
        if cxy is None:
            continue
        times.append(t)
        xs.append(cxy[0] - centre_x)
    times = np.array(times)
    xs = np.array(xs)

    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "synth.csv")
        save_track_csv(path, times, xs, np.full_like(xs, centre_y))
        rows = np.loadtxt(path, delimiter=",", skiprows=1)
        t_loaded, x_loaded = rows[:, 0], rows[:, 1]

    p0 = [100.0, 2.0 * math.pi * 0.5, 0.0, 5.0]
    popt, _pcov = curve_fit(damped_sine, t_loaded, x_loaded, p0=p0, maxfev=10000)
    a_fit, omega_fit, phase_fit, tau_fit = popt

    assert abs(abs(a_fit) - truth["amplitude"]) / truth["amplitude"] < 0.05
    assert abs(omega_fit - truth["omega"]) / truth["omega"] < 0.05
    assert abs(tau_fit - truth["tau"]) / truth["tau"] < 0.10
