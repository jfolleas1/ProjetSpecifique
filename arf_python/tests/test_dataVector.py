## ----------------------------------------------------------------------------
# Import
import unittest
from arf_python.DataVector import DataVector
from arf_python.Point import Point
import os
## ----------------------------------------------------------------------------
# Constant
PATH_REPO = "./arf_python/tests"
NAME_FILE = "data.csv"

class RandomTest(unittest.TestCase):

    """Test on the ARF algorithm"""
    def test_dataVector(self):
        data_vector = DataVector(2,  NAME_FILE)
        self.assertEqual(data_vector.get_size_of_data(), 250, "the size is not good")

    def test_dataVector_point_list(self):
        data_vector_test = DataVector(2, NAME_FILE)
        self.assertEqual(len(data_vector_test.get_points()), 250, "the size is not good")

    def test_dataVector_points(self):
        data_vector1 = DataVector(2, NAME_FILE)
        data_vector2 = DataVector(2, NAME_FILE)

        list_point = data_vector2.get_points()
        for index, point in enumerate(data_vector1.get_points()):
            self.assertEqual(list_point[index], point, "the point are not equal.")


