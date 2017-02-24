# -*- coding: utf-8 -*-

import unittest
import sys


class BasicTestSuite(unittest.TestCase):
    def test_python_versions(self):
        assert sys.version_info[0] == 2
        assert sys.version_info[1] == 7


if __name__ == '__main__':
    unittest.main()