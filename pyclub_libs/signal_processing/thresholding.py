import math
import warnings

import numpy as np

from margrie_libs.signal_processing.exceptions import PeakDetectionError

# TEST: check usage limitations and document
def find_levels(wave, threshold):  # REFACTOR: rename to find_positive_level_crossings or similar or add boolean parameter for direction
    """
    Find the points in wave that cross threshold with a positive crossing (positive slope)

    :param np.array wave:
    :param float threshold:
    :return:
    """
    mask = wave < threshold  # TODO: do for positive or negative
    starts_mask = find_range_starts(mask)
    indices = np.where(starts_mask == 1)  # convert to indices
    return indices[0]


def find_range_starts(src_mask):
    """
    For a binary mask of the form:
    (0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,1)
    returns:
    (0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1)
    """
    tmp_mask = np.logical_and(src_mask[1:], np.diff(src_mask))
    output_mask = np.hstack(([src_mask[0]], tmp_mask))  # reintroduce first element
    return output_mask


def find_level_increase(trace, value):  # TODO: find better numpy built in function (try numpy.where(condition)[0][0]
    for i in range(1, len(trace)):
        if trace[i-1] < value <= trace[i]:
            return i
    raise StopIteration("value {} not found".format(value))


def find_level_decrease(trace, value):  # TODO: find better numpy built in function (try numpy.where(condition)[0][0]
    for i in range(1, len(trace)):
        if trace[i-1] > value >= trace[i]:
            return i
    raise StopIteration("value {} not found".format(value))


def count_points_between_values(pnt_a, pnt_b, src_array):
    """
    Counts the number of points separating pnt_a and pnt_b in src_array

    .. warning::

        Cases where pnt_a and pnt_b appear multiple times are not handled


    :param pnt_a: The first value to consider
    :param pnt_b: The second value to consider
    :param src_array: The array to search
    :return: The number of points between the index of pnt_a and the index of pnt_b
    """
    start = min(pnt_a, pnt_b)
    end = max(pnt_a, pnt_b)
    src_array = np.array(src_array, ndmin=1)
    levels = src_array[(src_array >= start) & (src_array < end)]
    n_levels = len(levels)
    return n_levels


def find_sine_peaks_ranges(sine_trace):
    """
    Sine has to be zero centered
    """
    return abs(sine_trace) > (0.9 * sine_trace.max())


def find_sine_peaks(sine_trace):
    """
    Returns the indices (points) of the peaks
    Sine has to be zero centered
    """
    peak_ranges = find_sine_peaks_ranges(sine_trace)

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        boundaries = np.diff(peak_ranges)
    boundaries_indices = (np.where(boundaries == True))[0]

    peak_starts = boundaries_indices[::2]
    peak_starts += 1  # add 1 because of diff
    peak_ends = boundaries_indices[1::2]
    peak_ends += 1  # add 1 because of diff

    peaks_pos = []
    for peak_start, peak_end in zip(peak_starts, peak_ends):
        peak = abs(sine_trace[peak_start:peak_end])  # abs because positive and negative peaks
        peak_pos = np.where(peak == peak.max())[0]   # because there may be several points at max
        if 0 in peak:
            raise PeakDetectionError('There should be no 0 in the peak, found {}'.format(peak))
        middle = int(math.floor(peak_pos.size / 2))
        if peak_pos.size % 2 == 0:
            middle -= 1
        peak_pos = peak_pos[middle]
        peak_pos += peak_start  # absolute position
        peaks_pos.append(peak_pos)
    return peaks_pos
