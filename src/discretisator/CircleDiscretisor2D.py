# -------- Aim of the file

# This file provide an class to dicretise points by using the circle methode

# -------- Import
from src.discretisator.Discretisator import Discretisator
import math
import numpy as np
from numpy.linalg import inv


from src.structureData.Point import Point
import src.util.Constants as Constants
# --------- Constant



# --------- Code



class CircleDiscretisator2D(Discretisator):
    """
    This class is an implementation of Dicretisator for a "rectangle" discrtisation.
    Args :
    :param lambda_error: float representing how each coordinates of the points should be ceil or floor.
    """


    def __init__(self, lambda_error, methode=Constants.DIS_TESTS):
        def __get_space_base(lambda_error):
            triangle_side = math.sqrt(3) * 2 * lambda_error
            u1 = np.array([triangle_side, 0])
            u2 = np.array([(triangle_side / 2), (math.sqrt(3) * triangle_side / 2)]) ##
            transition_matrix_u_to_e = np.array([[triangle_side, (triangle_side / 2)], [0,
                                                               (math.sqrt(3) * triangle_side / 2)]])
            transition_matrix_e_to_u = inv(transition_matrix_u_to_e)
            return u1, u2, transition_matrix_e_to_u, transition_matrix_u_to_e

        Discretisator.__init__(self, lambda_error)
        u1, u2, e_to_u, u_to_e = __get_space_base(lambda_error)
        self.ray = (2 * lambda_error)/math.sqrt(3)
        self.u1 = u1
        self.u2 = u2
        self.transition_matrix_e_to_u = e_to_u
        self.transition_matrix_u_to_e = u_to_e
        self.methode = methode

    def change_base_e_to_u(self,point_coord):
        """

        :param point_coord: list of float tht are coordonate in e base
        :return: list of float tht are coordonate in u base
        """
        return list(np.transpose(np.dot(self.transition_matrix_e_to_u, np.transpose(np.array([point_coord]))))[0])

    def change_base_u_to_e(self,point_coord):
        """

        :param point_coord: list of float tht are coordonate in e base
        :return: list of float tht are coordonate in u base
        """
        return list(np.transpose(np.dot(self.transition_matrix_u_to_e, np.transpose(np.array([point_coord]))))[0])

    def four_points_around(self, point_coord_in_base_u):
        """

        :param point_coord_in_base_u:
        :return: tuple of for point that are around the point represented by the coordonate : point_coord_in_base_u
        """
        floored_x_coord = math.floor(point_coord_in_base_u[0])
        floored_y_coord = math.floor(point_coord_in_base_u[1])
        down_left = Point(list(np.transpose(np.dot(self.transition_matrix_u_to_e, np.array([[floored_x_coord],
                                                                                            [floored_y_coord]])))[0]))
        down_right = Point(list(np.transpose(np.dot(self.transition_matrix_u_to_e, np.array([[floored_x_coord+1],
                                                                                            [floored_y_coord]])))[0]))
        up_left = Point(list(np.transpose(np.dot(self.transition_matrix_u_to_e, np.array([[floored_x_coord],
                                                                                            [floored_y_coord+1]])))[0]))
        up_right = Point(list(np.transpose(np.dot(self.transition_matrix_u_to_e, np.array([[floored_x_coord+1],
                                                                                            [floored_y_coord+1]])))[0]))
        return (down_left, down_right, up_left, up_right)

    def get_three_closer_points(self, tuple_of_points, central_point):
        """
        Return the three colest points in tuple_of_points from central_point
        :param tuple_of_points: tuple of 4 points
        :param central_point: Point instance
        :return: list of 3 points
        """
        max_distance = 0
        repr_farest = ""
        for pt in tuple_of_points:
            if central_point.distance(pt) > max_distance:
                max_distance = central_point.distance(pt)
                repr_farest = pt.to_string()
        res = []
        for pt in tuple_of_points:
            if not pt.to_string() == repr_farest:
                res.append(pt)
        return res

    def get_closest_point(self, tuple_of_points, central_point):
        """
        Return the closest point in tuple_of_points from central_point
        :param tuple_of_points: tuple of 4 points
        :param central_point: Point instance
        :return: list of 3 points
        """
        min_distance = central_point.distance(tuple_of_points[0])
        closest_point = tuple_of_points[0]
        for pt in tuple_of_points:
            if central_point.distance(pt) < min_distance:
                min_distance = central_point.distance(pt)
                closest_point = pt
        return closest_point



    def discretize_in_multiple_points(self, point):
        assert isinstance(point, Point), "the point argument has to be a Point instance"
        assert len(point.coordinates) == 2, "The point has to be of dimension 2"
        point_coord = point.coordinates
        point_coord_in_base_u = self.change_base_e_to_u(point_coord)
        tuple_of_four_points_around = self.four_points_around(point_coord_in_base_u)
        return self.get_three_closer_points(tuple_of_four_points_around, point)

    def discretize_in_one_point(self, point):
        assert isinstance(point, Point), "the point argument has to be a Point instance"
        assert len(point.coordinates) == 2, "The point has to be of dimension 2"
        point_coord = point.coordinates
        point_coord_in_base_u = self.change_base_e_to_u(point_coord)
        tuple_of_four_points_around = self.four_points_around(point_coord_in_base_u)
        return self.get_closest_point(tuple_of_four_points_around, point)


    def discretise_point_to_test(self, point):
        if self.methode == Constants.DIS_TESTS:
            return self.discretize_in_multiple_points(point)
        elif self.methode == Constants.DIS_INPUTS:
            return [self.discretize_in_one_point(point)]
        else:
            raise NotImplementedError("This methode is not implemented with circle discretizor")

    def discretise_point_to_insert(self, point):
        if self.methode == Constants.DIS_INPUTS:
            return self.discretize_in_multiple_points(point)
        elif self.methode == Constants.DIS_TESTS:
            return [self.discretize_in_one_point(point)]
        else:
            raise NotImplementedError("This methode is not implemented with circle discretizor")