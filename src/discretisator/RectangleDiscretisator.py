# -------- Aim of the file

# This file provide an abstract class with method to frame a point

# -------- Import
from src.discretisator.Discretisator import Discretisator
from src.structureData.Point import Point
import decimal
from decimal import Decimal
from copy import deepcopy

# --------- Constant


# --------- Code
class RectangleDiscretisator(Discretisator):
    """
    This class is an implementation of Dicretisator for a "rectangle" discrtisation.
    Args :
    :param lambda_error: float representing how each coordinates of the points should be ceil or floor.
    """

    def __init__(self, lambda_error):
        Discretisator.__init__(self, lambda_error)

    def maximizePoint(self, point):
        """
        Apply a ceil to each coordinate of the given list in parameter
        Args :
        :param point: coordinates which have to be maximised
        """
        for i in range(0, len(point)):
            point[i] = Decimal(point[i]).quantize(self.lambda_error, decimal.ROUND_UP)
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
        results.append(Point(self.maximizePoint(point_c.coordinates)))
        self.discretise_recursive(point_c.coordinates, point.coordinates, 0, results)
        return results

    def discretise_recursive(self, point, original_point, starting_index, results):
        """
        shouldn't be called directly, call for discretise
        """
        for i in range(starting_index, len(point)):
            if point[i] != original_point[i]:
                #the original value of point should be the same for each passage in the loop  so deepcopy
                point_c = deepcopy(point) # TODO ????
                point_c[i] -= self.lambda_error
                results.append(Point(point_c))
                self.discretise_recursive(point_c, original_point, i+1, results)

    def discretise_point_to_one(self, point):
        list_pt = self.discretise_point(point)
        min_pt = list_pt.pop(0)
        min_dist = point.distance(min_pt)
        for pt in list_pt:
            if point.distance(pt) < min_dist:
                min_pt = pt
                min_dist = point.distance(pt)
        return min_pt
