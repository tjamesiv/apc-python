import matplotlib.pyplot as plt
import matplotlib.colors as py_colors
import numpy as np
import ipywidgets
from ipywidgets import widgets
from ipywidgets import IntSlider, fixed


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
            elif style == "pixels":
                plt.plot(complex_list[x].real, complex_list[x].imag, 'b,')
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


# def plot_complex(z):
#     plt.plot([0, z.real], [0, z.imag], 'b.-')
#     plt.show()


def plot_complex_grid(complex_list):


def render_plot(complex_list, num_iterations):
    print("Number of iterations = {}".format(num_iterations))
    plot_complex_list(complex_list[:num_iterations], style="points")


def round_complex(z):
    return "{0.real:.3}+{0.imag:.3}j".format(z)


def round_magnitude(z):
    return str(np.around(np.absolute(z), 3))
