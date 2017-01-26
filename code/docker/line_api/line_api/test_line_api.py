#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from os import path
APP_ROOT = path.dirname(path.abspath(__file__))
from line_api import LINE_API

sys.path.append('.')

class TestLineApi(unittest.TestCase):
    """
        This class verifies that PyGram.Profile is executing properly.
    """

    def setUp(self):
        self.line_api = LINE_API()

    def testCallBack(self):
        """
        Check call back method
        :return:
        """
        CHECK_VALUE = "OK"
        self.assertEqual(self.line_api.callback(), CHECK_VALUE)

    def testHandleMessage(self):
        """
        Check call back method
        :return:
        """
        CHECK_VALUE = "Test"
        self.line_api.handle_message(CHECK_VALUE)

if __name__ == "__main__":
   unittest.main()