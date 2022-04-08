# -*- coding: utf-8 -*-
"""
type definitions for dupuitflow

General Constants
^^^^^^^^^^^^^^^^^

.. autosummary::
   DupuitFlow_FileClasses

"""
from __future__ import division, print_function, absolute_import

# input files of dupuitflow
DupuitFlow_FileClasses = [
    "dupuitflowin",  # aquifer parameters
    "h1in",  # river stages over time
    "hinitialin",  # initial river stage
    "outputlocationsin",  # output locations
    "outputtimesin",  # output times
    "rin",  # recharge
]
"""list: all dupuitflow iput files"""
