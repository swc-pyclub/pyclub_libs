import sys
sys.path.insert(0, 'utils')
from debug_utils import log_all_variables


@log_all_variables()
def do_something():
    a = 10
    b = 20
    b = b*3
    c = b - a
    return c


do_something()

