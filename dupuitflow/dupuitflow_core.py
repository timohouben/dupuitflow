# -*- coding: utf-8 -*-
"""
Base Class for a dupuitflow model run.

.. currentmodule:: dupuitflow.dupuitflow_core

DupuitFlow Class
^^^^^^^^^^^^^^^^

.. autosummary::
   DupuitFlow

----
"""

from __future__ import absolute_import, division, print_function
import os
import shutil
import subprocess
from datetime import datetime

from dupuitflow.fileclasses.dupuitflowin import DupuitFlowIn
from dupuitflow.fileclasses.h1in import H1In
from dupuitflow.fileclasses.hinitialin import HinitialIn
from dupuitflow.fileclasses.outputlocationsin import OutputLocationsIn
from dupuitflow.fileclasses.outputtimesin import OutputTimesIn
from dupuitflow.fileclasses.rin import RIn

from dupuitflow.fileclasses.base import TOP_COM, CWD
from dupuitflow.tools.types import DupuitFlow_FileClasses


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
        self.comment = "None"
        # self._top_com = "User comment: " + str(self.comment) + " " + TOP_COM
        self.output_dir = output_dir
        self.exitstatus = None

        self.dupuitflowin = DupuitFlowIn(task_root=task_root, task_id=task_id)
        self.h1in = H1In(task_root=task_root, task_id=task_id)
        self.hinitialin = HinitialIn(task_root=task_root, task_id=task_id)
        self.outputlocationsin = OutputLocationsIn(task_root=task_root, task_id=task_id)
        self.outputtimesin = OutputTimesIn(task_root=task_root, task_id=task_id)
        self.rin = RIn(task_root=task_root, task_id=task_id)

    @property
    def top_com(self):
        """Get and set the top comment for the dupuitflow input files."""
        return self._top_com

    @top_com.setter
    def top_com(self, value):
        print("!!!" + str(self._top_com))
        self._top_com = value
        for file in DupuitFlow_FileClasses:
            # workaround to get access to class-members by name
            getattr(self, file).top_com = value

    @property
    def task_root(self):
        """Get and set the task_root path of the dupuitflow model."""
        return self._task_root

    @task_root.setter
    def task_root(self, value):
        self._task_root = value
        for file in DupuitFlow_FileClasses:
            # workaround to get access to class-members by name
            getattr(self, file).task_root = value

    @property
    def task_id(self):
        """:class:`str`: task_id (name) of the dupuitflow model."""
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        for file in DupuitFlow_FileClasses:
            # workaround to get access to class-members by name
            getattr(self, file).task_id = value

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
            # if not os.path.isabs(self._output_dir):
            #     # if not, put the outputfolder in the task_root
            #     self._output_dir = os.path.join(
            #         os.path.abspath(self.task_root), self._output_dir
            #     )

    def writeinput(self):
        """Method to call all writefile() methods that are initialized."""
        for file in DupuitFlow_FileClasses:
            # print("Wrote current dupuit model " + self.task_id)
            getattr(self, file).writefile()

    def reset(self):
        """Delete every content."""
        print("Not implemented.")
        pass

    def plot_modelling_results(self, pop_first=True, show=False):
        """
        Call plotting routines which correspond to the dupuitflow model.

        Parameters
        ----------
        path: string
            path to the modelling results. Subfolder must be "input_files"
            containing the input files and "output_files" containing the
            output_files.
        pop_first : bool, optional
            True : First value of time series (pertubation measure, aquifer scale
            hydraulic cond. and flux) at t = 0 will be set to np.nan since it can
            be very high.
        show : bool, optional
            If True plot will be shown.

        Yields
        ------
        A new folder called "plots" and a summary plot for a transient or a
        steady-state model run.
        """
        from dupuitflow.tools.plots import plot_summary_transient
        # check if mode ran
        if self._output_dir is None:
            raise RuntimeError("The model didn't run.")
        else:
            # check if 'path' contains foder 'input_files' with 'DupuiFlow.IN'
            # and return steady keyword
            from dupuitflow.reader.reader import steady_or_transient
            steady = steady_or_transient(os.path.join(self._output_dir, "input_files"))
            # steady = .....
            if steady is True:
                print("The model is a steady-state model. No plotting function implemented.")
                # CALL THAT OTHER FUNCTION FOR STEADY RUNS
                pass
            elif steady is False:
                plot_summary_transient(self._output_dir, pop_first, show)

    def load_dupuitflow_model():
        """
        Function to read input and output files of a dupuit flow model run.
        """
        pass

    def read_modelling_results(self, path=None, savetxt=True):
        """
        Function to call the read_modelling_results in reader.

        Parameters
        ----------
        path : str, optional
            The path to the results directory containing the folder
            "output_files" and "input_files". If None, the previously created
            folder will be taken.
        savetxt : bool, optional
            If True: txt-files of the results will be saved in the results
            diretory in folder txt.

        Returns
        -------
        h_array

        aquifer_scale_data


        """
        from dupuitflow.reader.reader import read_modelling_results

        if path is None:
            path = self._output_dir

        h_array, aquifer_scale_data = read_modelling_results(path, savetxt=savetxt)
        return h_array, aquifer_scale_data

    def run_model(self, path_exe=None):
        """
        Run the dupuitflow model which has been set up.

        Parameters
        ----------

        path_exe : str
            Path inlcuding file name of the groundwater model executable which
            has been compiled from de Rooij's F90 code.
        """
        # check if given path and file name was set and exists
        if path_exe is None:
            raise ValueError(
                "The path including name of the groundwaer model executable was not specified."
            )
        if not os.path.isfile(path_exe):
            raise FileNotFoundError(
                "The groundwater model executable which you specified does not exist."
            )
        # get the name of the directory from the executable
        dirname_path_exe = os.path.dirname(path_exe)
        # create an result folder with the task name and the times
        time_now = datetime.now()
        time_now_log = time_now.strftime("%Y-%m-%d_%H-%M-%S")
        self.output_dir = os.path.join(
            self.task_root, self.task_id + "_" + time_now_log
        )
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)
        # make directory for input files
        input_dir = os.path.join(self.output_dir, "input_files")
        if not os.path.exists(input_dir):
            os.mkdir(input_dir)
        # make directory for output files
        output_files_dir = os.path.join(self.output_dir, "output_files")
        if not os.path.exists(output_files_dir):
            os.mkdir(output_files_dir)
        # copy input files in the input_files folder in the result folder
        for file in os.listdir(self.task_root):
            if file.endswith(".IN"):
                shutil.copy(os.path.join(self.task_root, file), input_dir)
        # copy executable in input_files folder
        shutil.copy(path_exe, input_dir)
        # copy mods of executable in input_files folder
        for file in os.listdir(dirname_path_exe):
            if file.endswith(".mod"):
                shutil.copy(os.path.join(dirname_path_exe, file), input_dir)
        # change directory to input_dir since the F90 code need the CWD to
        # find the input files
        os.chdir(input_dir)
        # execute groundwater model
        print("Starting groundwater model ...")
        model_run = subprocess.run(path_exe)
        return_code = model_run.returncode
        if return_code != 0:
            print("Model run failed... ")
        else:
            print("Model run successfully finished!")
        # change directory back to CWD
        os.chdir(CWD)
        # copy output files in output_dir
        for file in os.listdir(input_dir):
            if file.endswith(".OUT"):
                print(file)
                print(os.path.join(input_dir, file))
                print(output_files_dir)
                shutil.move(os.path.join(input_dir, file), output_files_dir)
        # remove groundwater model executable
        os.remove(os.path.join(input_dir, os.path.basename(path_exe)))
        for file in os.listdir(input_dir):
            if file.endswith(".mod"):
                os.remove(os.path.join(input_dir, file))
        return return_code
