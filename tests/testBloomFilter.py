import unittest
from src.BloomFilter.BloomFilterTester import BloomFilterTester
from src.structureData.Point import Point
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
import src.discretisator.MethodType as Method

class PointTest(unittest.TestCase):
    """Test case used for test my Point class."""

    def setUp(self):
        """Initialize tests."""
        self.bf_tester = BloomFilterTester(20, 80, discretisator=RectangleDiscretisator(1, Method.DIS_DOUBLE))
        self.bf_tester.feed([Point([0.5, 0.5])])
        self.discretized_points = [Point([0.0, 0.0]), Point([1.0, 0.0]), Point([0.0, 1.0]), Point([1.0, 1.0])]

        self.bf_tester_before = BloomFilterTester(20, 80, discretisator=RectangleDiscretisator(10, Method.DIS_TO_INSERT))
        self.bf_tester_before.feed([Point([5, 5])])
        self.discretized_points_before = [Point([-10, -10]), Point([-10, 10]), Point([10, -10]), Point([10, 10])]

        self.bf_tester_after = BloomFilterTester(20, 80, discretisator=RectangleDiscretisator(10, Method.DIS_TO_INSERT))
        self.bf_tester_after.feed([Point([5, 5])])
        self.discretized_points_after = [Point([-10, -10]), Point([-10, 10]), Point([10, -10]), Point([10, 10])]

    def test_bf_size_double(self):
        """Test if bloom filter have the correct size"""
        self.assertEqual(80, self.bf_tester._get_bf_size())

    def test_insertion_each_point_double(self):
        """Test if the discretized vector are all well inserted"""
        for pt in self.discretized_points:
            self.assertEqual(True, self.bf_tester.test_one_point(pt))

    def test_test_set_points_double(self):
        """Test if the check a all set of point work"""
        self.assertEqual(4,self.bf_tester.test_set_points(self.discretized_points), "error in test_test_set_points")
        self.assertEqual(1, self.bf_tester.test_set_points([Point([1.6, 1.6])]), "error in test_test_set_points")
        self.assertEqual(0, self.bf_tester.test_set_points([Point([2, 1.6])]), "error in test_test_set_points")

    def test_insertion_each_point_before(self):
        """Test if the discretized vector are all well inserted"""
        for pt in self.discretized_points_before:
            self.assertEqual(True, self.bf_tester_before.test_one_point(pt))

    def test_test_set_points_before(self):
        """Test if the check a all set of point work"""
        self.assertEqual(4, self.bf_tester_before.test_set_points(self.discretized_points_before),
                         "error in test_test_set_points")
        self.assertEqual(1, self.bf_tester_before.test_set_points([Point([14, 14])]), "error in test_test_set_points")
        self.assertEqual(0, self.bf_tester_before.test_set_points([Point([21, 8])]), "error in test_test_set_points")

    def test_insertion_each_point_after(self):
        """Test if the discretized vector are all well inserted"""
        for pt in self.discretized_points_before:
            self.assertEqual(True, self.bf_tester_before.test_one_point(pt))

    def test_test_set_points_after(self):
        """Test if the check a all set of point work"""
        self.assertEqual(4, self.bf_tester_before.test_set_points(self.discretized_points_before),
                         "error in test_test_set_points")
        self.assertEqual(1, self.bf_tester_before.test_set_points([Point([14, 14])]), "error in test_test_set_points")
        self.assertEqual(0, self.bf_tester_before.test_set_points([Point([21, 8])]), "error in test_test_set_points")