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

    """

    def __init__(self, lambda_error):
        Discretisator.__init__(self, lambda_error)

    def maximizePoint(self, point):
        for i in range(0, len(point)):
            point[i] = Decimal(point[i]).quantize(self.lambda_error, decimal.ROUND_UP)
        return point

    def make_points(self, list_coordonates):
        res = []
        for coord in list_coordonates:
            float_coord = list(map((lambda x: float(x)), coord))
            res.append(Point(float_coord))
        return res

    def discretise_point(self, point):
        point_c = deepcopy(point) # TODO ???
        results = []
        results.append(self.maximizePoint(point_c.coordinates))
        self.discretise_recursive(point_c.coordinates, point.coordinates, 0, results)
        return self.make_points(results)

    def discretise_recursive(self, maximised_point, original_point, starting_index, results):
        for i in range(starting_index, len(maximised_point)):
            if maximised_point[i] != original_point[i]:
                point_c = maximised_point[:] # TODO ????
                point_c[i] -= self.lambda_error
                results.append(point_c)
                self.discretise_recursive(point_c, original_point, i+1, results)
