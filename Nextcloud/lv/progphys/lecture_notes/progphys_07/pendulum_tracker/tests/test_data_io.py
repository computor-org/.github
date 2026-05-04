import os
import tempfile

import numpy as np
import pytest

from pendulum_tracker.src.data_io import save_track_csv


def test_round_trip_preserves_values():
    t = np.linspace(0, 1, 5)
    x = np.array([10.0, 11.5, 13.2, 14.0, 13.7])
    y = np.array([60.0, 60.1, 59.9, 60.2, 60.0])
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "track.csv")
        save_track_csv(path, t, x, y)
        rows = np.loadtxt(path, delimiter=",", skiprows=1)
        t2, x2, y2 = rows[:, 0], rows[:, 1], rows[:, 2]
    np.testing.assert_allclose(t2, t)
    np.testing.assert_allclose(x2, x)
    np.testing.assert_allclose(y2, y)


def test_save_track_csv_rejects_mismatched_shapes():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "track.csv")
        with pytest.raises(ValueError):
            save_track_csv(path, np.zeros(5), np.zeros(4), np.zeros(5))


def test_round_trip_handles_nan():
    t = np.array([0.0, 0.1, 0.2])
    x = np.array([5.0, float("nan"), 7.0])
    y = np.array([60.0, 60.0, float("nan")])
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "track.csv")
        save_track_csv(path, t, x, y)
        rows = np.loadtxt(path, delimiter=",", skiprows=1)
        t2, x2, y2 = rows[:, 0], rows[:, 1], rows[:, 2]
    np.testing.assert_allclose(t2, t)
    assert np.isnan(x2[1])
    assert np.isnan(y2[2])
    assert x2[0] == 5.0
    assert y2[1] == 60.0
