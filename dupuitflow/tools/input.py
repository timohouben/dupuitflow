# -*- coding: utf-8 -*-
"""
Tools to check the input

General Constants
^^^^^^^^^^^^^^^^^

.. autosummary::
   content_checker

"""
from __future__ import division, print_function, absolute_import
import os


# check if the content is 1D list with integers or floats
def content_checker(content, filename):
    """
    Check if content is None and raise error if 'True'.
    """
    if content is None:
        raise ValueError("There is no content to write in " + filename)
    if not type(content) == list:
        raise ValueError("Please set a list with integers or floats as content.")
    for index, item in enumerate(content):
        if not isinstance(item, (float, int)):
            raise ValueError(
                "All entries must be floats or ints. Detected wrong entry at index "
                + str(index + 1)
            )


def check_results_status(path):
    """
    Check which status the the model currently has.

    Parameters
    ----------
    path : string
        Path to output directory of groundwater model.

    Returns
    -------
    status : string
        'no_folder'     : folder does not exist
        'no_output'     : output folder available but not 'output_files' and
                          'input_files'
        'ran'           : groundwater model ran, folder exists and contains a
                          folder with output 'output_files' files and a folder
                          with input files 'input_files'
        'read_results'  : results have been read and saved in output folder
                          'txt'
    """
    # # check if folder exists
    # if not os.path.exists(path):
    #     print("The specified folder does not exist.")
    #     status = 'no_folder'
    # elif not os.path.exists(os.path.join(path, 'output_folder')) or not os.path.exists(os.path.join(path, 'input_folder')):
    #     print("Either folder 'output_files' or 'input_files' not available under given path.")
    #     status = 'no_output'
    # elif
    #
    # path = "/Users/houben/Desktop/TEST/dupuitflow_ex_1_2020-03-24_16-06-42"
    # os.walk("/Users/houben/Desktop/TEST/dupuitflow_ex_1_2020-03-24_16-06-42")
    # for dirpath, dirnames, files in os.walk(path):
    #     print(dirnames, files)
    #     print("new")

    # return status
    pass
