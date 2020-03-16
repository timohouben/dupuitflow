# -*- coding: utf-8 -*-
"""
Purpose
=======

dupuitflow: a Python template.

Subpackages
===========

.. autosummary::
    core

"""
from __future__ import absolute_import

from dupuitflow._version import __version__
from dupuitflow.dupuitflow_core import DupuitFlow
from dupuitflow.fileclasses import DupuitFlowIn
from dupuitflow.fileclasses import H1In

__all__ = ["__version__"]
__all__ += ["core"]
