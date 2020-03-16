# -*- coding: utf-8 -*-
"""
type definitions for ogs5

General Constants
^^^^^^^^^^^^^^^^^

.. autosummary::
   OGS_EXT

"""
from __future__ import division, print_function, absolute_import

# input files of dupuitflow
DupuitFlow_FILES = [
    "Dupuitflow.in",  # aquifer parameters
    "H1.in",  # river stages over time
    "Hinitial.in",  # initial river stage
    "OutputLocations.in",  # output locations
    "OutputTimes.in",  # output times
    "R.in",  # recharge
]
"""list: all dupuitflow iput files"""
