shell_color_codes = {
    'black': (30, 40),
    'red': (31, 41),
    'green': (32, 42),
    'yellow': (33, 43),
    'blue': (34, 44),
    'magenta': (35, 45),
    'cyan': (36, 46),
    'white': (37, 47)
}


def dprint(input_str):
    """
    prints the input if in debug mode, skips otherwise.

    :param str input_str:
    """
    if __debug__:
        print(input_str)


def print_rule(thick=False, line_length=70):
    """
    Prints a line of - or = characters of default width 70 characters.
    
    :param bool thick: Whether to print a thin or thick line.
    :param int line_length: The number of characters to print.
    """
    symbol = '=' if thick else '-'
    print(symbol*line_length)


def shell_hilite(src_string, color, bold=True):
    """
    Formats the input string with ANSI escape codes for terminal formatting.
    
    >>> print("something in white, {} something else in white".format(shell_hilite("Something in red", "red")))

    :param str src_string: The string to highlight.
    :param str color: The color to print the string in (one of ('black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')).
    :param bool bold: Whether to print in bold characters.
    :return: The formatted string
    :rtype: str
    """
    color = color.lower()
    if color not in shell_color_codes.keys():
        raise AttributeError("Unknown color {}".format(color))
    color_params = [str(shell_color_codes[color][0])]
    if bold:
        color_params.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(color_params), src_string)
