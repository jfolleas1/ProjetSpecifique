import unittest
from src.structureData.Point import Point


class PointTest(unittest.TestCase):
    """Test case used for tests my Point class."""

    def setUp(self):
        """Initialize tests."""
        self.point_a = Point([1,2])
        self.point_b = Point([4,6])

    def test_distance(self):
        """Test of function distance."""
        dist = self.point_a.distance(self.point_b)
        self.assertEqual(5, dist)

    def test_zero_distance(self):
        """Test of function distance."""
        dist = self.point_a.distance(self.point_a)
        self.assertEqual(0, dist)