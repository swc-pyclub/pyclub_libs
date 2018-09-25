"""
This module is a wrapper around R statistics functions using rpy2 because
python (scipy) sometimes has incomplete statistics support or does
not have all the corrections.
"""

from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import FloatVector
r_stats = importr('stats')


class PyclubStatsValueError(ValueError):
    pass


def paired_t_test(vect1, vect2):
    try:
        p_val = r_stats.ttest_rel(vect1, vect2)[1]
    except ValueError as err:
        raise PyclubStatsValueError('vect1: {} ({} elements), vect2: {} ({} elements); {}'
                                    .format(vect1, len(vect1), vect2, len(vect2), err))
    return p_val


def wilcoxon_test(vect1, vect2, paired=True, exact=True, return_stat=False):
    """
    Perform the wilcoxon test on the 2 vectors

    :param vect1: The first input vector
    :param vect2: The second input vector
    :param bool paired: Paired wilcoxon test (default)
    :param bool exact:
    :param bool return_stat: Whether to get the test statistic as a second return value

    :raises PyclubStatsValueError: if the input vectors have different length.
    :return: The p value of the test
    """
    if len(vect1) == 0 or len(vect2) == 0:
        return float('nan')
    if paired and len(vect1) != len(vect2):
        raise PyclubStatsValueError("Arrays have different length: {}, {}".
                                    format(len(vect1), len(vect2)))
    try:
        results = r_stats.wilcox_test(FloatVector(vect1), FloatVector(vect2),
                                      paired=paired,
                                      exact=exact)
    except ValueError as err:
        raise PyclubStatsValueError('vect1: {} ({} elements), vect2: {} ({} elements); {}'
                                    .format(vect1, len(vect1), vect2, len(vect2), err))
    p_val = results[results.names.index('p.value')][0]
    wilcox_stat = results[results.names.index('statistic')][0]
    out = [p_val]
    if return_stat:
        out.append(wilcox_stat)
    return out
