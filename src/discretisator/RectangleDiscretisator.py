# -------- Aim of the file

# This file provide an abstract class with method to frame a point

# -------- Import
from src.discretisator.Discretisator import Discretisator
import decimal
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
            point[i] = point[i].quantize(self.lambda_error, decimal.ROUND_UP)
        return point


    def discretise_point(self, point):
        point_c = deepcopy(point) # TODO ???
        results = []
        results.append(self.maximizePoint(point.coordinates))
        self.discretise_recursive(point.coordinates, 0, results)
        return results



    def discretise_recursive(self, point, starting_index, results):
        for i in range(starting_index, len(point)):
            point_c = point[:] # TODO ????
            point_c[i] -= self.lambda_error
            results.append(point_c)
            self.discretise_recursive(point_c, i+1, results)