# dupuitflow
A python wrapper for a Fortran90 coded semi-analytical solution of the linearized Boussinesq equation evoking the Dupuit assumptions.

[![Documentation Status](https://readthedocs.org/projects/dupuitflow/badge/?version=latest)](https://dupuitflow.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.com/timohouben/dupuitflow.svg?branch=master)](https://travis-ci.com/timohouben/dupuitflow)
[![Coverage Status](https://coveralls.io/repos/github/timohouben/dupuitflow/badge.svg?branch=master)](https://coveralls.io/github/timohouben/dupuitflow?branch=master)
[![MIT License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# The Solution
The semi-analytical solution to a linearized Boussinesq equation evoking the Dupuit assumptions was derived by Gerrit de Rooij. A detailed explanation and the code (Fortran90) can be downloaded from his [official page](https://www.ufz.de/index.php?en=44055).
I would like to refer to the corresponding publication from 2012:

[Rooij, G.. (2012). **Transient flow between aquifers and surface water: analytically derived field-scale hydraulic heads and fluxes.** *Hydrology and Earth System Sciences.* 16. 10.5194/hess-16-649-2012.](https://www.researchgate.net/publication/307836186_Transient_flow_between_aquifers_and_surface_water_analytically_derived_field-scale_hydraulic_heads_and_fluxes)

For question related to the Fortran code please contact Gerrit de Rooij directly. For questions and remarks to the python wrapper please contact [Timo Houben](https://www.ufz.de/index.php?en=43660) or use the provided git services.

# Installation

#### 1. Compile the F90 code on your system
First, download the [fortran code](https://www.ufz.de/export/data/2/200312_Dupuitflow4.F90) from Gerrit de Rooij's page and compile it with a fortran compiler on your system. Follow [this link](https://gcc.gnu.org/wiki/GFortranBinaries) for infos on installation of the fortran compiler gcc.

Compile the F90 code:
```
gfortran 200312_Dupuitflow4.F90
```
If you are on Mac sometimes the following error occurs.
```
FATAL:/opt/local/bin/../libexec/as/x86_64/as: I don't understand 'm' flag!
```
The following fixed it for me.
```
export PATH=/usr/bin:$PATH
```
Try again!

When you successfully compiled the F90 file set the path to this file equal to the attribute in the method `DupuiFlow.run_model("path/to/executable")`.

#### 2. Install the dupuitflow package

Install python3.6 on your system. Download and unzip the repository. Open a terminal and change directory to the folder containing the `setup.py`.
```
cd PATH/TO/setup.py
```
Optionally, activate a virtual environment and install the dependencies.
```
pip install -r requirements.txt
```
Install dupuitflow package.
```
python3 setup.py install
```

# Examples

**WORKS ONLY FOR TRANSIENT SIMULATIONS**

You can set up the dupuit flow model with a script like the following one. It can be found [here](examples/example_1.py):

```python
# -*- coding: utf-8 -*-
"""
This is an example for a dupuitflow model setup.
"""
from dupuitflow import DupuitFlow
import numpy as np

task_root = "examples/dupuitflow_example_1"
task_id = "dupuitflow_ex_1"
exe = "PATH/TO/EXECUTABLE"
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
```

Besides some output files in a directory it produces the following plot:

![Summary plot for a transient model][summary_transient]

[summary_transient]: examples/testmodel1/plots/summary_transient.png "Summary plot"

# Acknowledgements
This package was build based upon the template from [Sebastian Mueller](https://github.com/MuellerSeb/template) and inspired by the structure of [ogs5py](https://github.com/GeoStat-Framework/ogs5py).
