import pytest

from pyclub_libs.logging import terminal


@pytest.mark.parametrize("test_input, test_color, bold, expected_output", [
    ('a', 'red', 1, '\x1b[31;1ma\x1b[0m'),
    ('a', 'blue', 1, '\x1b[34;1ma\x1b[0m'),
    ('a', 'blue', 0, '\x1b[34ma\x1b[0m')
])
def test_shell_format(test_input, test_color, bold, expected_output):
    assert terminal.shell_hilite(test_input, test_color, bold) == expected_output


def test_shell_format_raises():
    with pytest.raises(AttributeError):
        terminal.shell_hilite("a", "not_a_color")

