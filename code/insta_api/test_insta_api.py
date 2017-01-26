#!/usr/bin/env python
from __future__ import print_function
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from os import path
APP_ROOT = path.dirname(path.abspath(__file__))
from insta_api import InstaApi

sys.path.append('.')

class TestInstaApi(unittest.TestCase):
    """
        This class verifies that PyGram.Profile is executing properly.
    """

    def setUp(self):
        self.insta_api = InstaApi()

    def testTagSearch(self):
        """
        Check call Tag search method
        :return:
        """
        pass


if __name__ == "__main__":
    unittest.main()
