import pytest

from src.utils import utils
from src.exceptions import AutomatedBehaviourSystemException


@pytest.mark.parametrize("test_input, test_color, bold, expected_output", [
    ('a', 'red', 1, '\x1b[31;1ma\x1b[0m'),
    ('a', 'blue', 1, '\x1b[34;1ma\x1b[0m'),
    ('a', 'blue', 0, '\x1b[34ma\x1b[0m')
])
def test_shell_format(test_input, test_color, bold, expected_output):
    assert utils.shell_format(test_input, test_color, bold) == expected_output


def test_shell_format_raises():
    with pytest.raises(AutomatedBehaviourSystemException):
        utils.shell_format("a", "not_a_color")


@pytest.mark.parametrize("test_input, test_color, expected_output", [
    ("a", "red", '<span style="color:#FF0000">a</span>'),
    ("hello", "teal", '<span style="color:#008080">hello</span>')
])
def test_html_hilite(test_input, test_color, expected_output):
    assert utils.html_hilite(test_input, test_color) == expected_output


def test_html_hilite_raises():
    with pytest.raises(AutomatedBehaviourSystemException):
        utils.html_hilite("a", "not_a_color")