from pyclub_libs.logging.logging_decorators import log_all_variables


@log_all_variables()
def do_something():
    a = 10
    b = 20
    b = b*3
    c = b - a
    return c


def test_log_all_variables():
    do_something()
