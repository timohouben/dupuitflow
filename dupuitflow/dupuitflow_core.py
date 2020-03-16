# -*- coding: utf-8 -*-
"""
Base Class for a dupuitflow model run.

.. currentmodule:: ogs5py.dupuitflow

DupuitFlow Class
^^^^^^^^^^^^^^^^

.. autosummary::
   DupuitFlow

----
"""

from __future__ import absolute_import, division, print_function
import os

from dupuitflow.fileclasses.dupuitflowin import DupuitFlowIn
from dupuitflow.fileclasses.h1in import H1In
# from dupuitflow.fileclasses.hinitialin import HinitialIn
# from dupuitflow.fileclasses.outputlocationsin import OutputLocationsIn
# from dupuitflow.fileclasses.outputtimesin import OutputTimesIn
# from dupuitflow.fileclasses.rin import RIn

from dupuitflow.fileclasses.base import BOTTOM_COM




class DupuitFlow(object):
    """Class for a dupuitflow model.

    Use this class to set up a dupuitflow model run.

    Parameters
    ----------
    task_root : :class:`str`, optional
        Path to the destiny model folder.
        Default: cwd+"ogs5model"
    task_id : :class:`str`, optional
        Name for the ogs task.
        Default: "model"
    output_dir : :class:`str` or :class:`None`, optional
        Path to the output directory.
        Default: :class:`None`

    Notes
    -----
    The following Classes are present as attributes
        ZB  : EXAMPLE

    """

    def __init__(self, task_root=None, task_id="strip_aquifer", output_dir=None):
        if task_root is None:
            task_root = os.path.join(CWD, "dupuitflow_model")
        self._task_root = os.path.normpath(task_root)
        self._task_id = task_id
        self._output_dir = None
        self.output_dir = output_dir
        self.exitstatus = None

        self.dupuitflowin = DupuitFlowIn(task_root=task_root, task_id=task_id)
        # and so on ...

    @property
    def bottom_com(self):
        """Get and set the bottom comment for the dupuitflow input files."""
        return self._bottom_com

    @bottom_com.setter
    def bottom_com(self, value):
        self._bottom_com = value
        for file in DupuitFlow_FILES:
             # workaround to get access to class-members by name
            getattr(self, file[1:]).bottom_com = value

    @property
    def task_root(self):
        """Get and set the task_root path of the dupuitflow model."""
        return self._task_root

    @task_root.setter
    def task_root(self, value):
        self._task_root = value
        for file in DupuitFlow_FILES:
            # workaround to get access to class-members by name
            getattr(self, file[1:]).bottom_com = value

    @property
    def task_id(self):
        """:class:`str`: task_id (name) of the dupuitflow model."""
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        for file in DupuitFlow_FILES:
            getattr(self, file[1:]).task_id = value

    @property
    def output_dir(self):
        """:class:`str`: output directory path of the dupuitflow model."""
        return self._output_dir

    @output_dir.setter
    def output_dir(self, value):
        if value is None:
            self._output_dir = None
        else:
            self._output_dir = os.path.normpath(value)
            if not os.path.isabs(self._output_dir):
                # if not, put the outputfolder in the task_root
                self._output_dir = os.path.join(os.path.abspath(self.task_root), self._output_dir)

    def reset(self):
        """Delete every content."""
        print("Not implemented.")
        pass

    def write_input(self):
        """Method to call all write_file() methods that are initialized."""
        pass

    def read_Hout(self):
        """
        Reader for the H.OUT output file of the dupuitflow model.
        """
        pass

    def run_model():
        """
        Run the dupuitflow model which has been set up.
        """
        pass
