"""
Collection of generic numpy array functions
"""

import numpy as np

from margrie_libs.signal_processing.exceptions import BadRandomError


def cut_in_half(trace):
    middle = int(trace.size/2)
    first_half = trace[:middle]
    second_half = trace[middle:]
    if first_half.size != second_half.size:
        second_half = second_half[:-1]
    assert first_half.size == second_half.size, "Length of first half and second half differ: {} and {}".format(first_half.size, second_half.size)
    return first_half, second_half


def cut_and_avg_halves(trace):
    segments = cut_in_half(trace)
    return np.array(segments, dtype=np.float64).mean(0)


def out_of_place_shuffle(src_array):
    """
    A function to wrap the numpy shuffle function
    and not modify in place
    """
    if (src_array == 0).all():
        return src_array
    tmp = src_array.copy()
    np.random.shuffle(tmp)
    if (tmp == src_array).all():
        raise BadRandomError('Source array: {}\ntmpArray: {}'.format(src_array, tmp))
    return tmp


def shuffle_n_d(mat):
    """
    Returns the randomly shuffled version of the input array in all dimensions
    """
    if (mat == 0).all():
        return mat
    out = out_of_place_shuffle(mat.ravel())
    out.reshape(mat.shape)
    return out


def flip_odd_rows(mat):
    out = mat.copy()
    for i in range(1, mat.shape[1], 2):  # TEST: check that rows/col correct
        out[:, i] = mat[::-1, i]  # TEST: check that rows/col correct
    return out


def make_mask_from_indices(size, idx_true=None):
    """
    creates a boolean mask from a list or array of indices

    :param int size: the total size of the array
    :param list idx_true: a list of indices to be returned as True in the mask
    :return:
    """

    if idx_true is None:
        return np.ones(size, dtype=np.bool)

    mask = np.zeros(size, dtype=np.bool)
    mask[idx_true] = True
    return mask
