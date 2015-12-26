import matplotlib.pyplot as plt
import numpy as np
import ipywidgets
from ipywidgets import widgets
from ipywidgets import IntSlider, fixed

def plot_complex_list(complex_list):
    plt.grid(which='major')
    for x in range(len(complex_list)):
        plt.plot([0,complex_list[x].real],[0,complex_list[x].imag],'b.-')
    limit=np.max(np.ceil(np.absolute(complex_list)))
    plt.xlim((-limit,limit))
    plt.ylim((-limit,limit))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    ax = plt.subplot()
    ax.set_aspect('equal')
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()
    
def plot_complex(z):
    plt.plot([0,z.real],[0,z.imag],'b.-')
    plt.show()
    
def render_plot(complex_list, n):
    print("n = {}".format(n))
    plot_complex_list(complex_list[:n])