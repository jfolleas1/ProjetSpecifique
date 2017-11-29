import unittest
from src.structureData.Point import Point
from src.discretisator.CircleDiscretisor2D import CircleDiscretisator2D
import numpy as np
from numpy import linalg as la
import math


class CircleDiscretisatorTest(unittest.TestCase):
    """Test case used for test CircleDiscretisator class."""

    def setUp(self):
        """Initialize tests."""

        # For test_change_base_e_to_u
        self.discretisator1 = CircleDiscretisator2D(10)

        # For test_four_points_around
        self.discretisator2 = CircleDiscretisator2D(10)
        self.point_coord_in_base_u = [0.5, 0.5]

        # For test_get_three_closer_points & test_discretize_in_multiple_points1
        self.discretisator3 = CircleDiscretisator2D(10)
        self.central_point_coord_in_base_u31 = [0.1, 0.1]
        self.theorical_three_point_in_u31 = ([0.0, 0.0], [1.0, 0.0], [0.0, 1.0])
        self.central_point_coord_in_base_u32 = [0.9, 0.9]
        self.theorical_three_point_in_u32 = ([1.0, 0.0], [0.0, 1.0], [1.0, 1.0])

        # For test_get_three_descretized_points_around2 & test_discretize_in_one_point
        self.discretisator4 = CircleDiscretisator2D(10)
        self.central_point41 = Point(self.discretisator4.change_base_u_to_e([0.1, 0.1]))
        self.central_point42 = Point(self.discretisator4.change_base_u_to_e([0.9, 0.9]))
        self.central_point43 = Point(self.discretisator4.change_base_u_to_e([1.1, 0.1]))
        self.central_point44 = Point(self.discretisator4.change_base_u_to_e([0.1, 1.1]))

        # Only for test_discretize_in_one_point
        self.central_point45 = Point(self.discretisator4.change_base_u_to_e([0.9, 0.1]))
        self.central_point46 = Point(self.discretisator4.change_base_u_to_e([0.1, 0.9]))






    def test_change_base_e_to_u(self):
        assert (self.discretisator1.change_base_e_to_u(list(self.discretisator1.u1))) == [1.0, 0.0]
        assert (self.discretisator1.change_base_e_to_u(list(self.discretisator1.u2))[0]-0.0 < 1e-10) and\
                (self.discretisator1.change_base_e_to_u(list(self.discretisator1.u2))[0]-1.0 < 1e-10),\
                str(self.discretisator1.change_base_e_to_u(list(self.discretisator1.u2)))

    def test_four_points_around(self):
        def almost_equals(a, b):
            return la.norm(np.array(a.coordinates)-np.array(b.coordinates)) < 1e-10
        assert almost_equals(self.discretisator2.four_points_around(self.point_coord_in_base_u)[0], Point([0.0, 0.0])),\
                self.discretisator2.four_points_around(self.point_coord_in_base_u)[0].to_string()
        assert almost_equals(self.discretisator2.four_points_around(self.point_coord_in_base_u)[1], Point(list(\
                self.discretisator2.u1))), self.discretisator2.four_points_around(self.point_coord_in_base_u)[1].\
                to_string()
        assert almost_equals(self.discretisator2.four_points_around(self.point_coord_in_base_u)[2], Point(list(\
                self.discretisator2.u2))), self.discretisator2.four_points_around(self.point_coord_in_base_u)[2]. \
                to_string()
        assert almost_equals(self.discretisator2.four_points_around(self.point_coord_in_base_u)[3], Point(list( \
                self.discretisator2.u2+self.discretisator2.u1))), self.discretisator2.four_points_around(self.\
                point_coord_in_base_u)[3].to_string()

    def test_get_three_closer_points(self):
        def three_points_almost_equals(theroical_three_points, actual_three_points):
            def almost_equals(a, b):
                return la.norm(np.array(a.coordinates)-np.array(b.coordinates)) < 1e-10
            res = True
            for i in range(3):
                res = res and almost_equals(theroical_three_points[i], actual_three_points[i])
            return res
        theroical_three_points1 = list(map((lambda x: Point(self.discretisator3.change_base_u_to_e(x))),\
                                           self.theorical_three_point_in_u31))
        actual_three_points1 = self.discretisator3.get_three_closer_points(self.discretisator3.four_points_around(\
            self.central_point_coord_in_base_u31), Point(self.discretisator3.change_base_u_to_e(\
            self.central_point_coord_in_base_u31)))
        assert three_points_almost_equals(theroical_three_points1, actual_three_points1), str(actual_three_points1)
        theroical_three_points2 = list(map((lambda x: Point(self.discretisator3.change_base_u_to_e(x))), \
                                           self.theorical_three_point_in_u32))
        actual_three_points2 = self.discretisator3.get_three_closer_points(self.discretisator3.four_points_around( \
            self.central_point_coord_in_base_u32), Point(self.discretisator3.change_base_u_to_e( \
            self.central_point_coord_in_base_u32)))
        assert three_points_almost_equals(theroical_three_points2, actual_three_points2),\
            str(theroical_three_points2) + "\n"+str(actual_three_points2)

    def test_discretize_in_multiple_points1(self):
        def three_points_almost_equals(theroical_three_points, actual_three_points):
            def almost_equals(a, b):
                return la.norm(np.array(a.coordinates)-np.array(b.coordinates)) < 1e-10
            res = True
            for i in range(3):
                res = res and almost_equals(theroical_three_points[i], actual_three_points[i])
            return res
        theroical_three_points1 = list(map((lambda x: Point(self.discretisator3.change_base_u_to_e(x))),\
                                           self.theorical_three_point_in_u31))
        actual_three_points1 = self.discretisator3.discretize_in_multiple_points(Point(\
                    self.discretisator3.change_base_u_to_e(self.central_point_coord_in_base_u31)))
        assert three_points_almost_equals(theroical_three_points1, actual_three_points1), str(actual_three_points1)
        theroical_three_points2 = list(map((lambda x: Point(self.discretisator3.change_base_u_to_e(x))), \
                                           self.theorical_three_point_in_u32))
        actual_three_points2 = self.discretisator3.discretize_in_multiple_points(Point( \
            self.discretisator3.change_base_u_to_e(self.central_point_coord_in_base_u32)))
        assert three_points_almost_equals(theroical_three_points2, actual_three_points2), str(actual_three_points2)

    def test_discretize_in_multiple_points2(self):
        def almost_equals(a, b):
            return la.norm(np.array(a.coordinates) - np.array(b.coordinates)) < 1e-10

        tuple1 = self.discretisator4.discretize_in_multiple_points(self.central_point41)
        tuple2 = self.discretisator4.discretize_in_multiple_points(self.central_point42)
        tuple3 = self.discretisator4.discretize_in_multiple_points(self.central_point43)
        tuple4 = self.discretisator4.discretize_in_multiple_points(self.central_point44)

        assert almost_equals(tuple1[1], tuple2[0]), str(tuple1[1]) + "    " + str(tuple2[0])
        assert almost_equals(tuple1[1], tuple3[0]), str(tuple1[1]) + "    " + str(tuple3[0])
        assert almost_equals(tuple1[2], tuple2[1]), str(tuple1[2]) + "    " + str(tuple2[1])
        assert almost_equals(tuple1[2], tuple4[0]), str(tuple1[2]) + "    " + str(tuple4[0])

    def test_discretize_in_one_point(self):
        def almost_equals(a, b):
            return la.norm(np.array(a.coordinates) - np.array(b.coordinates)) < 1e-10

        closest_dis_point1 = self.discretisator4.discretize_in_one_point(self.central_point41)
        closest_dis_point2 = self.discretisator4.discretize_in_one_point(self.central_point42)
        closest_dis_point3 = self.discretisator4.discretize_in_one_point(self.central_point45)
        closest_dis_point4 = self.discretisator4.discretize_in_one_point(self.central_point46)

        assert almost_equals(closest_dis_point1, Point([0, 0])), str(closest_dis_point1) + "    " + str(Point([0, 0]))
        assert almost_equals(closest_dis_point2, Point(self.discretisator4.change_base_u_to_e([1, 1]))),\
                             str(closest_dis_point2) + "    " + str(Point([1, 1]))
        assert almost_equals(closest_dis_point3, Point(self.discretisator4.change_base_u_to_e([1, 0]))), \
            str(closest_dis_point3) + "    " + str(Point([1, 0]))
        assert almost_equals(closest_dis_point4, Point(self.discretisator4.change_base_u_to_e([0, 1]))), \
            str(closest_dis_point4) + "    " + str(Point([0, 1]))


