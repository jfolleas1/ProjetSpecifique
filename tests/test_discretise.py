import unittest
from src.structureData.Point import Point
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
from decimal import Decimal
from copy import deepcopy

class DiscretisatorTest(unittest.TestCase):
    """Test case used for test my discretisator class."""

    def setUp(self):
        """Initialize tests."""
        self.point_b = Point([Decimal('1.01'), Decimal('2.004')])
        self.point_a = Point([Decimal('1.01'), Decimal('2.004'), Decimal('3.88'), Decimal('4.9')])
        self.point_c = Point([Decimal('1.01'), Decimal('2.004'), Decimal('3.88'), Decimal('4.9')])
        self.discretisator = RectangleDiscretisator(0.1)

    def test_maximise(self):
        """Test of function distance."""
        self.discretisator.maximizePoint(self.point_a.coordinates)
        self.assertEqual(self.point_a.coordinates, [Decimal('1.1'), Decimal('2.1'), Decimal('3.9'), Decimal('4.9')])


    def test_discretise_rectangel(self):
        print self.discretisator.discretise_point(self.point_b)
        print self.discretisator.discretise_point(self.point_c)

