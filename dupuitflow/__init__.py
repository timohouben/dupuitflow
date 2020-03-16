# -*- coding: utf-8 -*-
"""
Purpose
=======

dupuitflow: a Python template.

Subpackages
===========

.. autosummary::
    dupuitflow_core
    fileclasses
    tools
    reader

"""
from __future__ import absolute_import

from dupuitflow._version import __version__
from dupuitflow.dupuitflow_core import DupuitFlow
from dupuitflow.fileclasses import DupuitFlowIn
from dupuitflow.fileclasses import H1In
from dupuitflow.fileclasses import HinitialIn
from dupuitflow.fileclasses import OutputLocationsIn
from dupuitflow.fileclasses import OutputTimesIn
from dupuitflow.fileclasses import RIn

__all__ = ["__version__"]
__all__ += ["core"]
