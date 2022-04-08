# -*- coding: utf-8 -*-
"""Class for the dupuitflow initial head file."""
from __future__ import absolute_import, division, print_function
from dupuitflow.fileclasses.base import ParameterFiles
import os


class DupuitFlowIn(ParameterFiles):
    """
    Class for the dupuitflow DupuitFlow.IN file.
    """

    def __init__(self, **dupuitflow_setup):
        super(DupuitFlowIn, self).__init__(**dupuitflow_setup)
        self._filename = "DupuitFlow.IN"
        self.K = None
        self.D = None
        self.L = None
        self.mu = None
        self.a = 0
        self.b = 0
        self.steady = True
        self.maxn = 10000
        self.interval = 20
        self.tolerance = 0.0001
        self.nroutputlocations = None
        self.nroutputtimes = None
        self.nrlochini = None
        self.nrtimesh1 = None
        self.nrtimesr = None



    def writefile(self):
        """
        Write the current DupuitFlow.IN file to the given folder.
        Its path is given by "task_root+task_id+file_ext".
        """
        # create the file path
        if not os.path.exists(self.task_root):
            os.makedirs(self.task_root)

        # check if all required attributes have been set
        if self.K is None:
            raise ValueError("Required parameter K hasn't been set so far...")
        if self.D is None:
            raise ValueError("Required parameter D hasn't been set so far...")
        if self.L is None:
            raise ValueError("Required parameter L hasn't been set so far...")
        if self.mu is None:
            raise ValueError("Required parameter mu hasn't been set so far...")

        with open(os.path.join(self.task_root, self._filename), "w") as file:
            file.write(self.top_com)
            file.write(
                "K             D             L             mu            a             b\n"
            )

            # file.write("{:4e}    \n".format(self.K))
            file.write(
                "{:4e}  {:4e}  {:4e}  {:4e}  {:4e}  {:4e}\n".format(
                    self.K, self.D, self.L, self.mu, self.a, self.b
                )
            )
            file.write("Steady or non-steady flow\n")
            if self.steady:
                file.write("Steady\n")
            else:
                file.write("nonsteady\n")
            file.write("NrOutputLocations    NrOutputTimes    Maxn  Interval Tolerance\n")
            file.write(
                "{:0.0f}    {:0.0f}    {:0.0f}    {:0.0f}    {:4e}\n".format(
                    self.nroutputlocations, self.nroutputtimes, self.maxn, self.interval, self.tolerance
                )
            )
            file.write("NrLocHini  NrTimesH1  NrTimesR\n")
            file.write(
                "{:0.0f}    {:0.0f}    {:0.0f}\n".format(
                    self.nrlochini, self.nrtimesh1, self.nrtimesr 
                )
            )
        return print("Wrote file DupuitFlow.IN")

    def __repr__(self):
        """Representation."""
        print("set the follwing attributes: TBD")
        return "set the follwing attributes: TBD"
