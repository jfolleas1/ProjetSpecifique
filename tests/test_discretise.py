import unittest
from src.structureData.Point import Point
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
from decimal import Decimal


class DiscretisatorTest(unittest.TestCase):
    """Test case used for test my discretisator class."""

    def setUp(self):
        """Initialize tests."""
        self.point_a = Point([Decimal('1.01'), Decimal('2.004')])
        self.point_b = Point([Decimal('1.01'), Decimal('2.004'), Decimal('4.9')])
        self.point_c = Point([Decimal('6.01'), Decimal('8.004')])
        self.discretisator = RectangleDiscretisator(0.1)
        self.discretisatorj = RectangleDiscretisator(1)
        self.point_j = Point([Decimal('0.5'), Decimal('0.5'), Decimal('0.5')])

    def test_maximise(self):
        """Test of function distance."""
        self.discretisator.maximizePoint(self.point_a.coordinates)
        self.assertEqual(self.point_a.coordinates, [Decimal('1.1'), Decimal('2.1')])

    def test_discretise_rectangle(self):
        result_1 = self.discretisator.discretise_point(self.point_a)
        result_2 = self.discretisator.discretise_point(self.point_b)
        self.assertEqual(len(result_1), 4)
        self.assertEqual(result_1, [Point([Decimal('1.1'), Decimal('2.1')]), Point([Decimal('1.0'), Decimal('2.1')]), Point([Decimal('1.0'), Decimal('2.0')]), Point([Decimal('1.1'), Decimal('2.0')])])
        self.assertEqual(len(result_2), 4)
        self.assertEqual(result_2, [Point([Decimal('1.1'), Decimal('2.1'), Decimal('4.9')]), Point([Decimal('1.0'), Decimal('2.1'), Decimal('4.9')]), Point([Decimal('1.0'), Decimal('2.0'), Decimal('4.9')]), Point([Decimal('1.1'), Decimal('2.0'), Decimal('4.9')])])



    def test_discretise_set(self):
        result = self.discretisator.discretise_point_set([self.point_a, self.point_c])
        self.assertEqual(len(result), 8)
        self.assertEqual(result, [Point([Decimal('1.1'), Decimal('2.1')]), Point([Decimal('1.0'), Decimal('2.1')]), Point([Decimal('1.0'), Decimal('2.0')]), Point([Decimal('1.1'), Decimal('2.0')]), Point([Decimal('6.1'), Decimal('8.1')]), Point([Decimal('6.0'), Decimal('8.1')]), Point([Decimal('6.0'), Decimal('8.0')]), Point([Decimal('6.1'), Decimal('8.0')])])


    def test_discretise_jacques(self):
        print()
        print("TEST JACUQES : ")
        print(self.discretisatorj.discretise_point(self.point_j))
        print()