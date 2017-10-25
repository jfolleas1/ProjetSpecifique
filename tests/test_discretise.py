import unittest
from src.structureData.Point import Point
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator



class DiscretisatorTest(unittest.TestCase):
    """Test case used for test my discretisator class."""

    def setUp(self):
        """Initialize tests."""
        self.point_a = Point([1.01, 2.004])
        self.point_b = Point([1.01, 2.004, 4.9])
        self.point_c = Point([6.01, 8.004])
        self.discretisator = RectangleDiscretisator(0.1)
        self.discretisatorj = RectangleDiscretisator(1)
        self.point_j = Point([0.5, 0.5, 0.5])

        self.point_d = Point(['1.01', '2.004'])
        self.point_e = Point(['1.01', '2.004', '4.9'])

    def test_maximise(self):
        """Test of function distance."""
        self.discretisator.maximizePoint(self.point_d.coordinates)
        self.discretisator.maximizePoint(self.point_e.coordinates)
        self.assertEqual(self.point_d.coordinates, [1.1, 2.1])
        self.assertEqual(self.point_e.coordinates, [1.1, 2.1, 4.9])

    def test_discretise_rectangle(self):
        result_1 = self.discretisator.discretise_point(self.point_a)
        result_2 = self.discretisator.discretise_point(self.point_b)
        print(result_2)
        self.assertEqual(len(result_1), 4)
        self.assertEqual(result_1, [Point([1.1, 2.1]), Point([1.0, 2.1]), Point([1.0, 2.0]), Point([1.1, 2.0])])
        self.assertEqual(len(result_2), 4)
        self.assertEqual(result_2, [Point([1.1, 2.1, 4.9]), Point([1.0, 2.1, 4.9]), Point([1.0, 2.0, 4.9]), Point([1.1, 2.0, 4.9])])



    def test_discretise_set(self):
        result = self.discretisator.discretise_point_set([self.point_a, self.point_c])
        self.assertEqual(len(result), 8)
        self.assertEqual(result, [Point([1.1, 2.1]), Point([1.0, 2.1]), Point([1.0, 2.0]), Point([1.1, 2.0]), Point([6.1, 8.1]), Point([6.0, 8.1]), Point([6.0, 8.0]), Point([6.1, 8.0])])


    def test_discretise_jacques(self):
        print()
        print("TEST JACUQES : ")
        print(self.discretisatorj.discretise_point(self.point_j))
        print()