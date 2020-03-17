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

# Acknowledgements
This package was build based upon the template from [Sebastian Mueller](https://github.com/MuellerSeb/template) and heavily inspired by the structure of [ogs5py](https://github.com/GeoStat-Framework/ogs5py).
