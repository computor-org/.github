"""CSV round-trip for tracked (t, x, y) data.

Format: a single header row 't,x,y' followed by one row per frame.
Coordinates are floats. Missing detections are stored as 'nan'.

The format is the smallest thing that round-trips exactly through
numpy.loadtxt / numpy.savetxt with a comma delimiter. No pandas.
"""
import os
import numpy as np


def save_track_csv(path, t, x, y):
    """Write three equal-length arrays to CSV with a 't,x,y' header."""
    t = np.asarray(t, dtype=float)
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    rows = np.column_stack([t, x, y])
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    np.savetxt(path, rows, delimiter=",", header="t,x,y", comments="")


def load_track_csv(path):
    """Read a 't,x,y' CSV. Returns three 1-D float arrays."""
    rows = np.loadtxt(path, delimiter=",", skiprows=1)
    return rows[:, 0], rows[:, 1], rows[:, 2]


def sine_sidecar_path(csv_path):
    """Path for the sine-params sidecar next to csv_path."""
    stem, _ = os.path.splitext(csv_path)
    return stem + ".sine.csv"


def save_sine_params(csv_path, A, omega, phi):
    """Save fitted sine parameters as <stem>.sine.csv next to csv_path."""
    path = sine_sidecar_path(csv_path)
    np.savetxt(path, [[float(A), float(omega), float(phi)]],
               delimiter=",", header="A,omega,phi", comments="")


def load_sine_params(csv_path):
    """Load sine params from <stem>.sine.csv. Returns [A, omega, phi] or None."""
    path = sine_sidecar_path(csv_path)
    if not os.path.exists(path):
        return None
    row = np.loadtxt(path, delimiter=",", skiprows=1)
    return [float(row[0]), float(row[1]), float(row[2])]
