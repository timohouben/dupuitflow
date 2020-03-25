# -*- coding: utf-8 -*-
"""Class for the dupuitflow initial head file."""
from __future__ import absolute_import, division, print_function
from dupuitflow.fileclasses.base import TwoColumnFiles


class HinitialIn(TwoColumnFiles):
    """
    Class for the dupuitflow Hinitial.IN file.
    """

    def __init__(self, **dupuitflow_setup):
        super(HinitialIn, self).__init__(**dupuitflow_setup)
        self._filename = "Hinitial.IN"

    pass
