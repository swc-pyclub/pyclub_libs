import numpy as np
from scipy.signal import savgol_filter


def box_smooth(y, box_pts):
    """
    A thin wrapper around numpy to do box smoothing

    :param y:
    :param box_pts:
    :return:
    """
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')  # TODO: check mode
    return y_smooth


def diff(a1, a2, shift):
    """
    Compute the diff after shifting array a2 by shift
    Contrary to the numpy version, the amount of shift can be specified
    """
    if len(a1) != len(a2):
        raise ValueError("Diff, input arrays must be same length, got {} and {}".format(len(a1), len(a2)))
    return a1[:(-shift)] - a2[shift:]


def high_pass(trace, n_pnts_high_pass_filter):
    trend = box_smooth(trace, n_pnts_high_pass_filter)
    return trace - trend


def low_pass(vector, n_pnts=51):
    polynomial_order = 3
    return savgol_filter(vector, n_pnts, polynomial_order)
