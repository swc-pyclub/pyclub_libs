"""
Create simple test data
"""
import numpy as np


def make_sine_x_y(n_points=1000000, duration=10, phy=0):
    """
    Makes the x and y components of a sine (e.g. to plot and use as sample data for test)

    :param int n_points:
    :param float duration: seconds
    :param phy:
    :return: cmd, sine_x
    """
    sine_x = np.linspace(0, duration, n_points)
    max_angle = 180
    freq = 0.1
    # phy = 3/2*np.pi
    sine_y = max_angle * np.sin(2*np.pi*freq*sine_x + phy)
    return sine_x, sine_y
