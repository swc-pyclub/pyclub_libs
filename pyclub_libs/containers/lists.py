import numpy as np


def flatten(lst):
    """
    this is the fastest implementation

    >>> flatten([[1, 2, 3], [2, 4, 6], [4, 6, 8]])
    [1, 2, 3, 2, 4, 6, 4, 6, 8]
    """
    out = []
    for sublist in lst:
        out.extend(sublist)
    return out


def sort_by(list_to_sort, list_to_sort_by, descend=True):
    """
    sort one list by another list

    >>> sort_by([1, 2, 3], [4, 1, 3], descend=False)
    [2, 3, 1], [1, 3, 4]

    :param list list_to_sort:
    :param list list_to_sort_by:
    :param bool descend:
    :return list sorted_list:
    """

    sorted_lists = [(cid, did) for did, cid in sorted(zip(list_to_sort_by, list_to_sort))]
    if descend:
        sorted_lists = sorted_lists[::-1]
    ordered = np.array(sorted_lists)[:, 0]
    ordered_by = np.array(sorted_lists)[:, 1]

    return list(ordered), list(ordered_by)


def to_sep_str(in_list, sep=','):
    """
    Return a sep (character or string) separated string from in_list

    >>> to_sep_str(['a', 'b', 'c'], '__')
    'a__b__c'
    >>> to_sep_str(range(3), ';')
    '0;1;2'

    :param in_list:
    :param sep:
    :return:
    """
    return sep.join([str(e) for e in in_list])
