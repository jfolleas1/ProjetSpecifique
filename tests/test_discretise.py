import unittest
from src.structureData.Point import Point
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator



class DiscretisatorTest(unittest.TestCase):
    """Test case used for test my discretisator class."""

    def setUp(self):
        """Initialize tests."""

        self.discretisator = RectangleDiscretisator(5)
        """"For minimize"""


        self.point_a = Point([7])
        self.point_b = Point([5])
        self.point_c = Point([10])
        self.point_d = Point([1, 32])
        self.point_e = Point([5, 10])


        """"For discrette"""
        self.point_f = Point([7])
        self.point_g = Point([5])
        self.point_h = Point([10])
        self.point_i = Point([1, 32])
        self.point_j = Point([5, 10])




    def test_maximise(self):
        """Test of function distance."""
        self.discretisator.minimisePoint(self.point_a.coordinates)
        self.discretisator.minimisePoint(self.point_b.coordinates)
        self.discretisator.minimisePoint(self.point_c.coordinates)
        self.discretisator.minimisePoint(self.point_d.coordinates)
        self.discretisator.minimisePoint(self.point_e.coordinates)
        print("Minimize: ")
        print(self.point_a.coordinates)
        print(self.point_b.coordinates)
        print(self.point_c.coordinates)
        print(self.point_d.coordinates)
        print(self.point_e.coordinates)
        print()


    def test_discretise(self):
        """Test of function distance."""

        print("Discretise: ")
        print(self.discretisator.discretise_point(self.point_f))
        print(self.discretisator.discretise_point(self.point_g))
        print(self.discretisator.discretise_point(self.point_h))
        print(self.discretisator.discretise_point(self.point_i))
        print(self.discretisator.discretise_point(self.point_j))

