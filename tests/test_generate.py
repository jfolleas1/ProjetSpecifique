import unittest

from src.providerData.ReaderFromGenerator import RandomDataGenerator
from src.structureData.Point import Point


class PointTest(unittest.TestCase):
    """Test case used for test my Point class."""

    def setUp(self):
        """Initialize tests."""
        print('dfddf')
        self.point_a = Point([2,2])
        #self.point_b = Point([5,6])
        self.data_set = [self.point_a]
        self.r =RandomDataGenerator(2, 2, 10)

    def test_generate_domain(self):
        """Test of function distance."""
        self.assertEqual(1, 1)
        a = self.r.genarate_falses_domain(2, self.data_set)
        print(a)
        print(len(a))

