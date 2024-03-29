# -*- coding: utf-8 -*-
from dupuitflow import DupuitFlow
import numpy as np

task_root = "path/to/root/dir"
task_id = "testmodel1"
exe = "/Users/houben/phd/chs_and_others/Gerrit/gw_model/download_20220408/a.out"
testmodel = DupuitFlow(task_root=task_root, task_id=task_id)
# set parameters for DupuitFlow.IN
testmodel.dupuitflowin.K = 5
testmodel.dupuitflowin.D = 6
testmodel.dupuitflowin.L = 80
testmodel.dupuitflowin.mu = 0.2
testmodel.dupuitflowin.a = 0.001
testmodel.dupuitflowin.b = 0.0055
testmodel.dupuitflowin.steady = False
testmodel.dupuitflowin.nroutputlocations = 5
testmodel.dupuitflowin.nroutputtimes = 61
testmodel.dupuitflowin.maxn = 10000
testmodel.dupuitflowin.interval = 20
testmodel.dupuitflowin.tolerance = 0.001
testmodel.dupuitflowin.nrlochini = 2
testmodel.dupuitflowin.nrtimesh1 = 4
testmodel.dupuitflowin.nrtimesr = 6
# set OutputTimes.IN and OutputLocations.IN, OneColumnFiles
testmodel.outputtimesin.content = (
    np.linspace(0, 49, 50).tolist() + np.linspace(50, 100, 11).tolist()
)
testmodel.outputlocationsin.content = [0, 5, 15, 40.0, 80.0]
# set H1.IN, R.IN and Hinitial.In, TwoColumnFiles
testmodel.rin.content_c1 = [9.0, 10.2, 30.0, 33.5, 37.0, 100.0]
testmodel.rin.content_c2 = [0.000, 0.01, 0.000, 0.004, 0.0001, 0.000]
testmodel.hinitialin.content_c1 = [2, 79]
testmodel.hinitialin.content_c2 = [5, 5.2]
testmodel.h1in.content_c1 = [0, 20, 30, 100]
testmodel.h1in.content_c2 = [4.2, 5.5, 5.5, 4.5]
# write the input files
testmodel.writeinput()
# start the model runT
exit_code = testmodel.run_model(exe)
# extract the modelling reults from the standard output files and save them
# in a new directory. Return head time series and aquifer scale time series.
head_ts, aqs_ts = testmodel.read_modelling_results()
testmodel.plot_modelling_results(pop_first=True, show=True)
