# -*- coding: utf-8 -*-
"""Class for the dupuitflow initial head file."""
from __future__ import absolute_import, division, print_function
from dupuitflow.fileclasses.base import OneColumnFiles


class OutputTimesIn(OneColumnFiles):
    """
    Class for the dupuitflow OutputTimes.IN file.
    """

    def __init__(self, **dupuitflow_setup):
        super(OutputTimesIn, self).__init__(**dupuitflow_setup)
        self._filename = "OutputTimes.IN"

    pass
