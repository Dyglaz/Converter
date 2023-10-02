import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def test_convert_length(self):
        self.assertAlmostEqual(Converter.convert_length(10, 'in', 'm'), 0.254, 3)
        self.assertAlmostEqual(Converter.convert_length(2, 'ft', 'm'), 0.6096, 3)
        self.assertAlmostEqual(Converter.convert_length(3, 'yd', 'm'), 2.7432, 3)
        self.assertAlmostEqual(Converter.convert_length(5, 'mi', 'm'), 8046.72, 3)
        self.assertAlmostEqual(Converter.convert_length(20, 'mi', 'yd'), 35200, 3)