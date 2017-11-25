import unittest
from src.BloomFilter.BloomFilterTester import BloomFilterTester
from src.structureData.Point import Point
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator


class PointTest(unittest.TestCase):
    """Test case used for tests my Point class."""

    def setUp(self):
        """Initialize tests."""
        self.bf_tester = BloomFilterTester(10, 80)
        self.bf_tester.feed([Point([0.5, 0.5])], discretisator=RectangleDiscretisator(1))
        self.discretized_points = [Point([0.0, 0.0]), Point([1.0, 0.0]), Point([0.0, 1.0]), Point([1.0, 1.0])]

    def test_bf_size(self):
        """Test if bloom filter have the correct size"""
        self.assertEqual(80, self.bf_tester._get_bf_size())

    def test_insertion_each_point(self):
        """Test if the discretized vector are all well inserted"""
        for pt in self.discretized_points:
            self.assertEqual(True, self.bf_tester.test_one_point(pt))

    def test_test_set_points(self):
        """Test if the check a all set of point work"""
        self.assertEqual(4,self.bf_tester.test_set_points(self.discretized_points), "error in test_test_set_points")
