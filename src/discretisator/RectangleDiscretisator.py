# -------- Aim of the file

# This file provide an abstract class with method to frame a point

# -------- Import
from src.discretisator.Discretisator import Discretisator
from src.structureData.Point import Point
import src.util.Constants as Constants

from copy import deepcopy

# --------- Constants


# --------- Code
class RectangleDiscretisator(Discretisator):
    """
    This class is an implementation of Dicretisator for a "rectangle" discrtisation.
    Args :
    :param lambda_error: float representing how each coordinates of the points should be ceil or floor.
    """

    def __init__(self, lambda_error=0.001, method = Constants.DIS_DOUBLE):
        Discretisator.__init__(self, lambda_error, method)
        print(method)
        print(method + " * " +Constants.DIS_DOUBLE + " * " + Constants.DIS_TESTS
              + " * " +Constants.DIS_INPUTS)

    def minimisePoint(self, point):
        """
        Apply a ceil to each coordinate of the given list in parameter
        Args :
        :param point: coordinates which have to be maximised
        """

        if self.method_type == Constants.DIS_DOUBLE:
            for i in range(0, len(point)):
                ratio = int(point[i]/self.lambda_error)
                point[i] = ratio * self.lambda_error
        else:
            for i in range(0, len(point)):
                ratio = int(point[i]/self.lambda_error);
                if ratio%2 == 0:
                    point[i] = (ratio-1)*self.lambda_error
                else:
                    point[i] = ratio * self.lambda_error
        return point


    def discretise_point(self, point):
        """
        Apply a combinatory ceil and floor to each coordinate of the given point in parameter, according to the lambda_error.
        Return a list of points that enclose the given point in parameter, in function of the dimension of the point and the lambda_error
        Args :
        :param point: coordinates which have to be maximised
        """
        #deepcopy the point given in parmeter to prevent instruction to modify it and be able able to use it again without modification
        point_c = deepcopy(point)
        results = []
        results.append(Point(self.minimisePoint(point_c.coordinates)))
        self.discretise_recursive(point_c.coordinates, point.coordinates, 0, results)
        return results

    def discretise_recursive(self, point, original_points, starting_index, results):
        """
        shouldn't be called directly, call for discretise
        """
        for i in range(starting_index, len(point)):
            if point[i] != original_points[i]:
                #the original value of point should be the same for each passage in the loop  so deepcopy
                point_c = point[:]
                if self.method_type == Constants.DIS_DOUBLE:
                    point_c[i] += self.lambda_error
                else:
                    point_c[i] += 2 * self.lambda_error
                results.append(Point(point_c))
                self.discretise_recursive(point_c, original_points, i+1, results)

    def discretise_point_to_one(self, point):
        list_pt = self.discretise_point(point)
        min_pt = list_pt.pop(0)
        min_dist = point.distance(min_pt)
        for pt in list_pt:
            if point.distance(pt) < min_dist:
                min_pt = pt
                min_dist = point.distance(pt)
        return min_pt

    def discretise_point_to_insert(self, point):
        points_to_insert = []
        if self.method_type == Constants.DIS_TESTS:
            points_to_insert.append(self.discretise_point_to_one(point))
        else:
            for d_pt in self.discretise_point(point):
                points_to_insert.append(d_pt)
        return points_to_insert

    def discretise_point_to_test(self, point):
        points_to_test = []
        if self.method_type == Constants.DIS_INPUTS:
            points_to_test = [self.discretise_point_to_one(point)]
        else:
            points_to_test = self.discretise_point(point)
        return points_to_test
