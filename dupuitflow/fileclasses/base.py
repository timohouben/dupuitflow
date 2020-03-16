# -*- coding: utf-8 -*-
"""
Base Classes for the dupuitflow input files.

.. currentmodule:: ogs5py.fileclasses.base

File Classes
^^^^^^^^^^^^
.. autosummary::
   File

----
"""
from __future__ import print_function, division, absolute_import

import time
import os

from dupuitflow._version import __version__ as version

# current working directory
CWD = os.getcwd()
# Bottom Comment for io-files
BOTTOM_COM = (
    "|-- Written with dupuitflow ("
    + version
    + ") on: "
    + time.strftime("%Y-%m-%d_%H-%M-%S")
    + " --|"
)

class File(object):
    """
    File class with common functionality for input files.

    Parameters
    ----------
    task_root : :class:`str`, optional
        Path to the destination folder. Default is cwd+"dupuitmodel"
    task_id : :class:`str`, optional
        Name for the dupuitflow model task. Default: "strip_aquifer"
    file_ext : :class:`str`, optional
        extension of the file (with leading dot ".std")
        Default: ".std"
    """

    def __init__(self, task_root=None, task_id="model", file_ext=".std"):
        self._name = None
        self.name_from_id = True
        if task_root is None:
            task_root = os.path.join(CWD, "dupuitflow_model")
        self.task_root = task_root
        self.task_id = task_id
        self.bot_com = BOTTOM_COM
        # placeholder for later derived classes for each file-type
        self.file_ext = file_ext
        # if an existing file should be copied
        self.copy_file = None
        self.copy_path = None
        self._force = False
    pass
