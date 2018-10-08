import matplotlib.pyplot as plt
import numpy as np    

def fix_subplot_clims(fig, vlims=None):
    # Force all subplots in figure to share same color lims
    # If limits are None, find min/max across plots

    # Get limits (if not given)
    if vlims is None:
        vmax = np.finfo(np.float64).min
        vmin = np.finfo(np.float64).max

        for ax in fig.axes: 
            for im in ax.get_images():                            
                vmax = max(vmax, np.max(im._A))
                vmin = min(vmin, np.min(im._A)) 
    else:
        vmin = vlims[0]
        vmax = vlims[1]

    # Apply limits to each image
    for ax in fig.axes:
        for im in ax.get_images():
            im.set_clim(vmin=vmin, vmax=vmax) 


def imagesc(im, show_colorbar=True, clim=None):
    # show matrix as image with colour scale
    plt.axis("off")    
    plt.imshow(im);
    if show_colorbar:
        plt.colorbar()
    if clim is not None:
        plt.clim(clim)


def nanhist(x, *args, **kwargs):

    # plot 1D histogram, ignoring NaNs
    plt.hist(x[np.isfinite(x)], *args, **kwargs);


# from http://joseph-long.com/writing/colorbars/
# puts a colorbar alongside existing plot, without messing
# up existing layout
def colorbar(mappable):

    from mpl_toolkits.axes_grid1 import make_axes_locatable

    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    return fig.colorbar(mappable, cax=cax)


def add_unit_line(color='red'):
    # Add line y = x to current axis
    axes = plt.gca()
    xmin, xmax = axes.get_xlim()
    ymin, ymax = axes.get_ylim()

    start = min(xmin, ymin);
    finish = max(xmax, ymax);

    plt.plot([start, finish], [start, finish], color=color, linewidth=3);


def add_x_zero_line(color='red'):
    axes = plt.gca()
    ymin, ymax = axes.get_ylim()

    plt.plot([0, 0], [0, ymax], color=color);


def add_y_zero_line(color='red'):
    axes = plt.gca()
    xmin, xmax = axes.get_xlim()

    plt.plot([0, xmax], [0, 0], color=color);


def fewer_ticks():
    # halve the number of tick mark for quick adjustment
    ax=plt.gca()
    ax.set_xticks(ax.get_xticks()[::2])
    ax.set_yticks(ax.get_yticks()[::2])

    
def plot_print_linregress(x,y):
    # plot linear regression line, and print out stats
    from scipy import stats

    x = x.squeeze()
    y = y.squeeze()    
    mask = np.isfinite(x) & np.isfinite(y)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x[mask], y[mask])
    print('slope: {:0.5f} intercept: {:0.5f} r-squared: {:0.5f} p-val: {:0.5f} stderr: {:0.5f}'.format(
            slope, intercept, r_value**2, p_value, std_err))
    
    plt.plot(x, intercept + slope*x, 'g', linewidth=3, label='fitted line')


def plot_print_linregress_auto():
    # add linear regression line to current plot, and print stats

    ax = plt.gca()
    xy = ax.collections[0].get_offsets()
    plot_print_linregress(xy[:,0], xy[:,1])

