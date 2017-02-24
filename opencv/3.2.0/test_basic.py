# -*- coding: utf-8 -*-

import unittest
import cv2
import numpy as np
import matplotlib as mp


class BasicTestSuite(unittest.TestCase):
    def test_versions(self):
        assert cv2.__version__ == '3.2.0'
        assert np.__version__ == '1.12.0'
        assert mp.__version__ == '2.0.0'


if __name__ == '__main__':
    unittest.main()