import unittest
from src.structureData.Point import Point
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
import src.discretisator.MethodType as Method


class DiscretisatorTest(unittest.TestCase):
    """Test case used for test my discretisator class."""

    def setUp(self):
        """Initialize tests."""

        self.discretisator = RectangleDiscretisator(5, Method.DIS_DOUBLE)
        self.discretisator_before = RectangleDiscretisator(5, Method.DIS_TO_INSERT)
        """"For minimize"""
        self.point_a = Point([17])
        self.point_b = Point([5])
        self.point_c = Point([1, 32])

    def test_minimise_double(self):
        """Test of function distance."""
        min_a = self.discretisator.minimisePoint(self.point_a.coordinates)
        min_b = self.discretisator.minimisePoint(self.point_b.coordinates)
        min_c = self.discretisator.minimisePoint(self.point_c.coordinates)
        self.assertEqual([15], min_a)
        self.assertEqual([5], min_b)
        self.assertEqual([0, 30], min_c)


    def test_minimise_dis_before(self):
        """Test of function distance."""
        min_a = self.discretisator_before.minimisePoint(self.point_a.coordinates)
        min_b = self.discretisator_before.minimisePoint(self.point_b.coordinates)
        min_c = self.discretisator_before.minimisePoint(self.point_c.coordinates)
        self.assertEqual([15], min_a)
        self.assertEqual([5], min_b)
        self.assertEqual([-5, 25], min_c)

    def test_discretise_double(self):
        """Test of function distance."""

        dis_a = self.discretisator.discretise_point(self.point_a)
        dis_b = self.discretisator.discretise_point(self.point_b)
        dis_c = self.discretisator.discretise_point(self.point_c)
        self.assertEqual([Point([15]), Point([20])], dis_a)
        self.assertEqual([Point([5])], dis_b)
        #order normally doesn't matter but for now it does
        self.assertEqual([Point([0, 30]), Point([5, 30]), Point([5, 35]), Point([0, 35])], dis_c)

    def test_discretise_before(self):
        """Test of function distance."""

        dis_a = self.discretisator_before.discretise_point(self.point_a)
        dis_b = self.discretisator_before.discretise_point(self.point_b)
        dis_c = self.discretisator_before.discretise_point(self.point_c)
        self.assertEqual([Point([15]), Point([25])], dis_a)
        self.assertEqual([Point([5])], dis_b)
        #order normally doesn't matter but for now it does
        self.assertEqual([Point([-5, 25]), Point([5, 25]), Point([5, 35]), Point([-5, 35])], dis_c)