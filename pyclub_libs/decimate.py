import numpy as np


def _get_decimate_new_n_pnts(trace, window_width, end_method):
    methods = ("drop", "strict", "pad")
    n_remaining_points = trace.size % window_width
    if end_method == 'strict' and n_remaining_points != 0:
        raise ValueError(
            "The decimation factor does not create an exact point numbers and you have selected 'strict'")
    elif end_method == 'drop':
        n_samples_last_window = 0
    elif end_method == 'pad':
        n_samples_last_window = n_remaining_points if n_remaining_points <= 2 else 2  # TODO: find better name for 'pad'
    else:
        raise ValueError("end_method should be one of {}, got {}".
                         format(methods, end_method))
    n_complete_windows = trace.size // window_width
    new_n_pnts = n_complete_windows * 2 + n_samples_last_window
    return new_n_pnts


def decimate(trace, decimation_factor=10, end_method="drop"):
    """
    Decimate (reduce the number of points) of the source trace to plot the trace.
    To preserve the visual aspect of the trace, the algorithm takes the min and max on a sliding window defined by
    decimation_factor.

    .. important:
        This function is intended for plotting only. For other uses, see more appropriate downsampling methods.

    :param trace: The trace to decimate
    :param int decimation_factor: the number X such that trace.size = X * out.size
    :param string end_method: How to deal with the last points
    :return: A decimated copy of the trace
    """

    if not isinstance(decimation_factor, int):
        raise TypeError("Decimation factor should be an integer number. Got {}.".format(decimation_factor))
    if decimation_factor < 1:
        raise ValueError("Decimation factor needs to be at least 1 to get a window of 2. Got {}.".
                         format(decimation_factor))

    window_width = decimation_factor * 2

    new_n_pnts = _get_decimate_new_n_pnts(trace, window_width, end_method)

    out = np.zeros(new_n_pnts)
    for i, j in enumerate(range(0, new_n_pnts, 2)):  # by 2 because 1 min and 1 max for each window
        window_start_p = i * window_width
        window_end_p = int(window_start_p + window_width)
        if window_start_p > trace.size:
            raise RuntimeError("Array {}, of size {}, iteration {}, from {} to {} ({} points)".
                               format(trace, trace.shape, i, window_start_p, window_end_p, window_width))
        if window_end_p > trace.size:
            window_end_p = -1
        segment = trace[window_start_p:window_end_p]
        out[j] = segment.min()
        try:
            out[j+1] = segment.max()
        except IndexError:  # If trace.size % window_width == 1
            break
    return out


def decimate_x(x_trace, decimation_factor=10, end_method="drop"):
    window_width = decimation_factor * 2
    new_n_pnts = _get_decimate_new_n_pnts(x_trace, window_width, end_method)
    return np.linspace(x_trace[0], x_trace[-1], new_n_pnts)  # FIXME: adjust not exactly x_trace[-1] because of drop