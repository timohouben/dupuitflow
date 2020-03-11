# -*- coding: utf-8 -*-
"""
This is the unittest for dupuitflow.
"""
from __future__ import division, absolute_import, print_function

import unittest
from dupuitflow import __version__, core


class Test(unittest.TestCase):
    def setUp(self):
        self.version = __version__

    def test_dupuitflow(self):
        print(self.version)
        print(core.dummy_func(2))


if __name__ == "__main__":
    unittest.main()
