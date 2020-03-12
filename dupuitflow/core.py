# -*- coding: utf-8 -*-
"""
The core module of dupuitflow.

The following functions are provided

.. currentmodule:: dupuitflow.core

.. autosummary::
   dummy_func
"""
from __future__ import division, absolute_import, print_function

from dupuitflow import __version__


def dummy_func(dummy_arg=1, **kwargs):
    """
    A dummy function.

    Parameters
    ----------
    dummy_arg : TYPE, optional
        DESCRIPTION. The default is 1.
    **kwargs
        DESCRIPTION.

    Returns
    -------
    res : TYPE
        DESCRIPTION.

    """

    res = dummy_arg * __version__
    return res


def you_know_what():
    """Say hello to my lovely little girl.


    Parameters
    ----------
    example_filename : str
    example_copy : bool
    example_dtype : data-type
    example_iterable : iterable object
    example_shape : int or tuple of int
    example_files : list of str

    Returns
    -------
    int
        Description of anonymous integer return value.

    err_code : int
        Non-zero value indicates error code, or zero on success.
    err_msg : str or None
        Human readable error message, or None on success.

    Yields
    ------
    int
        Description of the anonymous integer return value.

    Raises
    ------
    LinAlgException
        If the matrix is not numerically invertible.

    See Also
    --------
    average : Weighted average
    func_a : Function a with its description.
    func_b, func_c_, func_d
    func_e

    Notes
    -----
    The FFT is a fast implementation of the discrete Fourier transform:

#    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

#    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
#       expert systems and adaptive co-kriging for environmental habitat
#       modelling of the Highland Haggis using object-oriented, fuzzy-logic
#       and neural-network techniques," Computers & Geosciences, vol. 22,
#       pp. 585-588, 1996.

    """


    eingabe = input("You know what?")
    print("I love and miss you, my little python programmer :-*")
    print("\n       .....           .....            \n   ,ad8PPPP88b,     ,d88PPPP8ba,        \n  d8P'      'Y8b, ,d8P'      'Y8b       \n dP'           '8a8'           `Yd      \n 8(              ''              )8      \n I8                             8I      \n  Yb,                         ,dP       \n   .8a,                     ,a8.        \n     .8a,                 ,a8.      \n       .Yba             adP.        \n         `Y8a         a8P'      \n           `88,     ,88'        \n             '8b   d8'      \n              '8b d8'       \n               `888'        \n                 .      \n")
