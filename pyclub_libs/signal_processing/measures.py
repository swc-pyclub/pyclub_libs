"""
Measure some metrics on the data (series, arrays...) like mean, sd ... before or after filtering
"""

import numpy as np

from pyclub_libs.signal_processing.filters import high_pass


def get_high_pass_sd(trace, n_pnts_high_pass_filter):
    """
    Get the SD of the detrended trace (this can e.g. give an estimate of the noise).

    :param trace:
    :param int n_pnts_high_pass_filter:
    :return:
    """
    return np.std(high_pass(trace, n_pnts_high_pass_filter))
