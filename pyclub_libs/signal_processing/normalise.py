import numpy as np


def normalise(src_array):
    """
    Normalise srcArray from 0 to 1
    """
    out_array = src_array.copy()
    out_array -= out_array.min()
    out_array /= out_array.max()
    return out_array


def normalise_around_zero(src_array, baseline_end, baseline_start=0):
    """
    Normalise trace to baseline
    by centering average(baseline) on 0 and to max == 1

    :param np.array src_array: The array to normalise
    :param int baseline_start: The start of the baseline (reference zero period) in points, defaults to 0
    :param int baseline_end: The start of the baseline  in points
    """
    out_array = src_array.copy()
    
    bsl = np.mean(out_array[baseline_start:baseline_end])
    out_array -= bsl
    out_array /= out_array.max()
    
    return out_array
