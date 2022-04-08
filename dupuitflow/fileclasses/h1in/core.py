# -*- coding: utf-8 -*-
"""Class for the dupuitflow initial head file."""
from __future__ import absolute_import, division, print_function
from dupuitflow.fileclasses.base import TwoColumnFiles


class H1In(TwoColumnFiles):
    """
    Class for the dupuitflow H1.IN file.
    """

    def __init__(self, **dupuitflow_setup):
        super(H1In, self).__init__(**dupuitflow_setup)
        self._filename = "H1.IN"

    pass
