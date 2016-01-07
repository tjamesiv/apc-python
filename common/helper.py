import matplotlib.pyplot as plt
import matplotlib.colors as py_colors
import numpy as np
import ipywidgets
from ipywidgets import widgets
from ipywidgets import IntSlider, fixed


fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 6.0
fig_size[1] = 6.0
plt.rcParams["figure.figsize"] = fig_size


# Make sure f has a keyword argument of max_iterations
def iterate_function_on_grid(f, c=0, limit=2, resolution=100,
                             max_iterations=20, zoom=False, boundary_box=[]):

    if zoom is True:
        xmin = boundary_box[0]  # -limit
        xmax = boundary_box[1]  # limit
        ymin = -boundary_box[2]  # limit
        ymax = -boundary_box[3]  # -limit
    else:
        # possibly x/y backwards
        xmax = ymin = limit
        xmin = ymax = -limit

    xx, yy = np.meshgrid(np.linspace(xmin, xmax, resolution + 1),
                         np.linspace(ymin, ymax, resolution + 1),
                         indexing='xy')
    coordinate_matrix = xx + 1j * yy

    vfunc = np.vectorize(f, excluded=['max_iterations', 'c'])

    if c == 0:
        my_grid = vfunc(coordinate_matrix, max_iterations=max_iterations)
    else:
        my_grid = vfunc(coordinate_matrix, max_iterations=max_iterations, c=c)

    return my_grid


# Also create a "zoom" version for xmin, etc
def plot_complex_grid(complex_grid, limit=2, color_gradient="Purples",
                      zoom=False, boundary_box=[]):

    if zoom is True:
        xmin = boundary_box[0]
        xmax = boundary_box[1]
        ymin = boundary_box[2]
        ymax = boundary_box[3]
    else:
        # possibly x/y backwards
        xmax = ymax = limit
        xmin = ymin = -limit

    fig, ax = plt.subplots()

    plt.ylabel('Imaginary')
    plt.xlabel('Real')

    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    plt.imshow(complex_grid, extent=[xmin, xmax, ymin, ymax],
               cmap=color_gradient, alpha=1, interpolation="none")
    plt.show()


# Need to be able to change the limits
# Or explicitly set x/y min/max
def plot_complex_list(complex_list, style="vectors", colors=False, limit=0):
    # plt.grid(which='major')
    for x in range(len(complex_list)):
        # print(str(complex_list[x][1]))
        if colors is True:
            plt.plot(
                complex_list[x][0].real,
                complex_list[x][0].imag,
                marker=',',
                # color=plt.cm.prism(complex_list[x][1]))
                color=py_colors.ColorConverter.to_rgb(
                    self=py_colors.ColorConverter,
                    arg=str(complex_list[x][1])))
        else:
            if style == "vectors":
                plt.plot(
                    [0, complex_list[x].real],
                    [0, complex_list[x].imag],
                    'b.-')
            elif style == "points":
                plt.plot(complex_list[x].real, complex_list[x].imag, 'bo')
            else:
                print("Style " + style + " not defined.")
                return

    if limit == 0:
        limit = np.max(np.ceil(np.absolute(complex_list)))

    plt.xlim((-limit, limit))
    plt.ylim((-limit, limit))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    ax = plt.subplot()
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()


def render_plot(complex_list, num_iterations):
    print("Number of iterations = {}".format(num_iterations))
    plot_complex_list(complex_list[:num_iterations], style="points")


def round_complex(z):
    return "{0.real:.3}+{0.imag:.3}j".format(z)


def round_magnitude(z):
    return str(np.around(np.absolute(z), 3))
