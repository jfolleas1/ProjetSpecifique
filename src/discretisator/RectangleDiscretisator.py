# -------- Aim of the file

# This file provide an abstract class with method to frame a point

# -------- Import
from src.discretisator.Discretisator import Discretisator
from src.structureData.Point import Point
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
        #deepcopy the point given in parmeter to prevent instruction to modify it and be able able to use it again without modification
        point_c = deepcopy(point)
        results = []
        results.append(Point(self.maximizePoint(point_c.coordinates)))
        self.discretise_recursive(point_c.coordinates, point.coordinates, 0, results)
        return results

    def discretise_recursive(self, point, original_point, starting_index, results):
        for i in range(starting_index, len(point)):
            if point[i] != original_point[i]:
                #For the next passage in the loop the original value of point is needed so deepcopy
                point_c = point[:] # TODO ????
                point_c[i] -= self.lambda_error
                results.append(Point(point_c))
                self.discretise_recursive(point_c, original_point, i+1, results)
