# -*- coding: utf-8 -*-
"""
definitions to plot the modelling results

General Constants
^^^^^^^^^^^^^^^^^

.. autosummary::
   read_modelling_results
   steady_or_transient
   get_numbers_from_file
"""
from __future__ import division, print_function, absolute_import
import re
import os
import numpy as np


def read_modelling_results(path, savetxt=True):
    """
    Read the modelling results and save it as txt.

    Parameters
    ----------
    path: string
        path to the modelling results. Subfolder must be "input_files"
        containing the input files and "output_files" containing the
        output_files.

    Yields
    ------
    A txt-file for every time series in the results/time_series folder if the
    model was a transient run.
    """
    # check if path is correct
    if path is None:
        raise RuntimeError("The model didn't run.")
    elif not os.path.exists(os.path.join(path, "input_files")):
        raise ValueError("The path you specified does not contain modelling results.")
    # initialize lists for head data
    time = []
    x_coord = []
    h = []
    # define variables and it's names
    variables_names = ["aqs_time", "aqs_average_H", "aqs_Q", "aqs_Kup", "aqs_P"]
    # check if moder run was steady or transient
    steady = steady_or_transient(os.path.join(path, "input_files"))
    # get the number of observation points and number of time steps
    n_locations = sum(
        1 for line in open(os.path.join(path, "input_files", "OutputLocations.IN"), "r")
    )
    n_times = sum(
        1 for line in open(os.path.join(path, "input_files", "OutputTimes.IN"), "r")
    )
    # initiate arrays for the time head series at different locations
    h_array = np.zeros([n_times, n_locations])
    time_array = np.zeros([n_times, n_locations])
    x_coord_array = np.zeros([n_times, n_locations])
    # load the data from the output files
    h_data = get_numbers_from_file(os.path.join(path, "output_files", "H.OUT"))
    # split up h_data
    for i in range(0, len(h_data)):
        time.append(float(h_data[i][0]))
        x_coord.append(float(h_data[i][1]))
        h.append(float(h_data[i][2]))
    # disentangle for every location
    if steady is True:
        raise NotImplementedError("Steady ist not implemented.")
        # TO BE DONE
    if steady is False:
        i = 0
        k = 0
        while i < n_times:
            j = 0
            while j < n_locations:
                h_array[i, j] = h[k]
                time_array[i, j] = time[k]
                x_coord_array[i, j] = x_coord[k]
                k = k + 1
                j = j + 1
            i = i + 1

    head_header = "Head time series for locations: " + "   ".join(
        [str(i) for i in np.unique(x_coord)]
    )
    if savetxt:
        if not os.path.exists(os.path.join(path, "txt")):
            os.mkdir(os.path.join(path, "txt"))
        # save head file
        np.savetxt(os.path.join(path, "txt", "head.txt"), h_array, header=head_header)
        aquifer_scale_data = np.genfromtxt(
            os.path.join(path, "output_files", "AquiferScale.OUT"), skiprows=2, missing_values = "************", filling_values = np.nan
        )
        # save aquifer scale files and time
        for name, i in zip(variables_names, range(0, len(variables_names))):
            np.savetxt(
                os.path.join(path, "txt", name + ".txt"), aquifer_scale_data[:, i]
            )
    return h_array, aquifer_scale_data


# helper functions
# ----------------


def steady_or_transient(path, filename="DupuitFlow.IN"):
    """
    Check if transient or steady state has been selected.

    Parameters
    ----------

    path: str
        Path to the input files.

    Returns
    -------

    steady: bool
        True: steady-state model run
        False: transient model run
    """
    steady = False
    steady_test_file = open(os.path.join(path, filename), "r")
    lst = []
    for line in steady_test_file:
        lst.append(line)
    if (
        str(lst[4]) == "STEADY\r\n"
        or str(lst[4]) == "Steady\r\n"
        or str(lst[4]) == "steady\r\n"
    ):
        steady = True
    return steady


def get_numbers_from_file(path, skip_lines=2):
    """
    Function to read a file line-wise and extract numbers.

    Parameters
    ----------

    path: str
        Path to the file including the filename.
    skip_lines: int
        Number of lines to skipp at the beginning of the file.

    Returns
    -------

    lst: list
        A list with sepereated entries for found numbers.

    """
    with open(path, "r") as data_file:
        lst = []
        for string in data_file:
            line = re.findall(
                "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", string
            )
            lst.append(line)
        del lst[0:skip_lines]
    return lst
