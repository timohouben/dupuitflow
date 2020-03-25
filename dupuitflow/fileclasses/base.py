# -*- coding: utf-8 -*-
"""
Base Classes for the dupuitflow input files.

.. currentmodule:: ogs5py.fileclasses.base

File Classes
^^^^^^^^^^^^
.. autosummary::
   File
   ParameterFiles
   OneColumnFiles
   TwoColumnFiles

----
"""
from __future__ import print_function, division, absolute_import

import time
import os
from dupuitflow._version import __version__ as version
from dupuitflow.tools.input import content_checker

# current working directory
CWD = os.getcwd()
# Bottom Comment for io-files
TOP_COM = (
    "|-- Written with dupuitflow ("
    + version
    + ") on: "
    + time.strftime("%Y-%m-%d_%H-%M-%S")
    + " --|\n"
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

    def __init__(self, task_root=None, task_id="strip_aquifer", file_ext=".std"):
        self._name = None
        self.name_from_id = True
        if task_root is None:
            task_root = os.path.join(CWD, "dupuitflow_model")
        self.task_root = task_root
        self.task_id = task_id
        self.top_com = TOP_COM

    '''
    @property
    def name(self):
        """:class:`str`: name of the file without extension."""
        if self.name_from_id:
            return self.task_id
        return self._name

    @name.setter
    def name(self, value=None):
        if value is None:
            self.name_from_id = True
            self._name = None
        else:
            self._name = str(value)
            self.name_from_id = False

    @property
    def file_path(self):
        """:class:`str`: save path of the file."""
        return os.path.join(self.task_root, self.name + self.file_ext)

    @property
    def file_name(self):
        """:class:`str`: base name of the file with extension."""
        return os.path.basename(self.file_path)
    '''


class ParameterFiles(File):
    """
    Class for the parameter file.
    """

    def __init__(self, task_root=None, task_id="strip_aquifer"):
        super(ParameterFiles, self).__init__(task_root, task_id)

    pass


class OneColumnFiles(File):
    """
    Class for one column input files.
    """

    def __init__(self, task_root=None, task_id="strip_aquifer"):
        super(OneColumnFiles, self).__init__(task_root, task_id)
        self.content = None

    def writefile(self):
        # create the file path
        if not os.path.exists(self.task_root):
            os.makedirs(self.task_root)

        content_checker(self.content, self._filename)

        with open(os.path.join(self.task_root, self._filename), "w") as file:
            for line in self.content:
                file.write("{:8e}\n".format(line))
        print("Wrote file " + self._filename)


class TwoColumnFiles(File):
    """
    Class for two column input files.
    """

    def __init__(self, task_root=None, task_id="strip_aquifer"):
        super(TwoColumnFiles, self).__init__(task_root, task_id)
        self.content_c1 = None
        self.content_c2 = None

    def writefile(self):
        # create the file path
        if not os.path.exists(self.task_root):
            os.makedirs(self.task_root)

        content_checker(self.content_c1, self._filename)
        content_checker(self.content_c2, self._filename)

        with open(os.path.join(self.task_root, self._filename), "w") as file:
            for c1, c2 in zip(self.content_c1, self.content_c2):
                file.write("{:8e}    {:8e}\n".format(c1, c2))
        print("Wrote file " + self._filename)
