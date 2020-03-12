# -*- coding: utf-8 -*-
"""
Purpose
=======

dupuitflow: a Python template.

Subpackages
===========

.. autosummary::
    core
    test_dupuitflow

"""
from __future__ import absolute_import

from dupuitflow._version import __version__
from dupuitflow import core
from dupuitflow import test_dupuitflow

__all__ = ["__version__"]
__all__ += ["core"]
