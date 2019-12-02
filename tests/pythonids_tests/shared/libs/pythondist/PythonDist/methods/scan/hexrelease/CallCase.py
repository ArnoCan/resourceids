# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = "5624dc41-775a-4d17-ac42-14a0d5c41d1a"

__docformat__ = "restructuredtext en"

import unittest

import pythonids.pythondist
from pythonids.pythondist import \
    PYE_CPYTHON, PYE_IPYTHON, PYE_JYTHON, PYE_PYPY, PYE_IRONPYTHON
from testdata.pythonids_testdata import _fetch_pydist_to_32bit


class CallUnits(unittest.TestCase):


    def setUp(self):
        self.maxDiff = None

    def testCase010(self):
        self.assertTrue(
            _fetch_pydist_to_32bit() in (PYE_CPYTHON, PYE_IPYTHON, PYE_IRONPYTHON, PYE_JYTHON, PYE_PYPY),
            "Platform not supported"
            )

        pp = pythonids.pythondist.PythonDist()
        pp.scan()         
        hx = pp.get_hexrelease()
        self.assertEqual(
            pp.hexrelease,
            hx
        )


if __name__ == '__main__':
    unittest.main()
