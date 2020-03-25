# -*- coding: utf-8 -*-
"""
definitions to plot the modelling results

General Constants
^^^^^^^^^^^^^^^^^

.. autosummary::
   plot_summary_transient

"""
from __future__ import division, print_function, absolute_import
import matplotlib.pyplot as plt
import os
import numpy as np


def plot_summary_transient(path, pop_first=True, show=False):
    """
    Plot a summary plot for transient model runs.

    Parameters
    ----------
    path: string
        path to the modelling results. Subfolder must be "input_files"
        containing the input files and "output_files" containing the
        output_files.
    pop_first : bool, optional
        True : First value of time series (pertubation measure, aquifer scale
        hydraulic cond. and flux) at t = 0 will be set to np.nan since it can
        be very high.
    show : bool, optional
        If True plot will be shown.
    """
    from dupuitflow.reader.reader import steady_or_transient
    # check if path is correct
    if not os.path.exists(os.path.join(path, "txt")):
        raise ValueError(
            "The path you specified does not contain extracted modelling results. Run 'DupuitFlow.read_modelling_results' first."
        )
    # check if it contains a folder with DupuitFlow.in file and
    # get steady keyword
    try:
        steady = steady_or_transient(os.path.join(path, "input_files"))
    except FileNotFoundError:
        print("Cannot open 'DupuitFlow.in' in 'input_files'.")
        raise
    # check if it was a transient model run
    if steady is True:
        print(
            "Cannot plot transient summary plot for steady model results. Plotting steady instead."
        )
        raise NotImplementedError("Not implemented yet.")
    # make directory for plots
    if not os.path.exists(os.path.join(path, 'plots')):
        os.mkdir(os.path.join(path, 'plots'))
    elif steady is False:
        # load variables to plot from files
        Y = np.loadtxt(
            os.path.join(path, "input_files", "OutputLocations.IN"), skiprows=0
        )
        Y = np.tile(Y, [61, 1])
        Z = np.loadtxt(os.path.join(path, "txt", "head.txt"), skiprows=1)
        X = np.loadtxt(os.path.join(path, "txt", "aqs_time.txt"), skiprows=0)
        X = np.tile(X, [5, 1]).transpose()
        aqs_average_H = np.loadtxt(
            os.path.join(path, "txt", "aqs_average_H.txt"), skiprows=0
        )
        aqs_P = np.loadtxt(os.path.join(path, "txt", "aqs_P.txt"), skiprows=0)
        aqs_Q = np.loadtxt(os.path.join(path, "txt", "aqs_Q.txt"), skiprows=0)
        aqs_Kup = np.loadtxt(os.path.join(path, "txt", "aqs_Kup.txt"), skiprows=0)
        if pop_first is True:
            aqs_P[0], aqs_Q[0], aqs_Kup[0] = np.nan, np.nan, np.nan
            print("First value of pertubation measure, aquifer scale hydraulic cond. and flux has been set to np.nan.")
        # format matplotlib plot
        plt.style.use("ggplot")
        plt.tight_layout()
        # create figure
        fig = plt.figure(figsize=(20, 10))
        fig.suptitle("Results summary for transient model run " + os.path.dirname(path))
        # plot 3d wireframe
        ax1 = fig.add_subplot(1, 2, 1, projection="3d")
        ax1.plot_wireframe(X, Y, Z, rstride=1, cstride=0)
        ax1.set_title("head over time and location")
        ax1.view_init(40, 130)
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Location")
        ax1.set_zlabel("Head")
        # plot average head
        ax2 = fig.add_subplot(2, 4, 3)
        ax2.plot(X[:, 0], aqs_average_H)
        ax2.set_title("Average Head")
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Head")
        # plot pertubation
        ax3 = fig.add_subplot(2, 4, 4)
        ax3.plot(X[:, 0], aqs_P)
        ax3.set_title("Perturbation Measure")
        ax3.set_xlabel("Time")
        ax3.set_ylabel("Perturbation")
        # plot flux
        ax4 = fig.add_subplot(2, 4, 7)
        ax4.plot(X[:, 0], aqs_Q)
        ax4.set_title("Flux")
        ax4.set_xlabel("Time")
        ax4.set_ylabel("Flux")
        # plot aqs hydrauic cond
        ax5 = fig.add_subplot(2, 4, 8)
        ax5.plot(X[:, 0], aqs_Kup)
        ax5.set_title("Aquifer-scale Hydraulic Conductivity")
        ax5.set_xlabel("Time")
        ax5.set_ylabel("Conductivity")
        # padding in subplots
        plt.subplots_adjust(
            top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35
        )
        # save figure
        fig.savefig(os.path.join(path, 'plots', 'summary_transient.png'), dpi=600)
        # HIER WEITRER MACHEN
        if show is True:
            plt.show()


def plot_summary_steady(path, show=False):
    """
    Plot a summary plot for steady-state model runs.

    Parameters
    ----------
    path: string
        path to the modelling results. Subfolder must be "input_files"
        containing the input files and "output_files" containing the
        output_files.
    show : bool, optional
        If True plot will be shown.
    """
    # check if path is correct
    if not os.path.exists(os.path.join(path, "txt")):
        raise ValueError(
            "The path you specified does not contain extracted modelling results. Run 'DupuitFlow.read_modelling_results' first."
        )
    #
    # fig, ax = plt.subplots(figsize=(5, 5))
    # ax.plot(x_coord, h)
    # ax.set_title("steady state head")
    # ax.set_xlabel('location')
    # ax.set_ylabel('head [m]')
    # ax.annotate('average H = ' + str(averageH), xy=(2, 1), xytext=(max(x_coord)-30, max(h)))
    # ax.annotate('Q = ' + str(Q), xy=(2, 1), xytext=(max(x_coord)-30, max(h)-20))
    # ax.annotate('Kup = ' + str(Kup), xy=(2, 1), xytext=(max(x_coord)-30, max(h)-40))
    # ax.annotate('P = ' + str(P), xy=(2, 1), xytext=(max(x_coord)-30, max(h)-60))
    # fig.savefig('plots.png')
    #
    # if show is True:
    #      plt.show()

def plot_time_series():
    """
    Plot the time series for all observation points
    """
    # else:
    #     fig, ax = plt.subplots(figsize=(5, 5))
    #     ax.plot(x_coord, h)
    #     ax.set_title("steady state head")
    #     ax.set_xlabel('location')
    #     ax.set_ylabel('head [m]')
    #     ax.annotate('average H = ' + str(averageH), xy=(2, 1), xytext=(max(x_coord)-30, max(h)))
    #     ax.annotate('Q = ' + str(Q), xy=(2, 1), xytext=(max(x_coord)-30, max(h)-20))
    #     ax.annotate('Kup = ' + str(Kup), xy=(2, 1), xytext=(max(x_coord)-30, max(h)-40))
    #     ax.annotate('P = ' + str(P), xy=(2, 1), xytext=(max(x_coord)-30, max(h)-60))
    #     fig.savefig('plots.png')
    #     plt.show()
    #
    # return fig
    pass
