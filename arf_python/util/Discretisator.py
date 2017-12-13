# -------- Aim of the file

# This file provide an abstract class with method to dicscretise a point

# -------- Import

from abc import ABCMeta, abstractmethod
from decimal import Decimal
import src.util.Constants as Constants

# --------- Constant


# --------- Code
class Discretisator:
    """
    This class is the interface for all data discretisators.
    Args :
    :param lambda_error: float representing how each coordinates of the points should be ceil or floor.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, lambda_error=0.01, method_type=Constants.DIS_TESTS):
        self.lambda_error = lambda_error
        self.method_type = method_type

    def discretise_point(self, point):
        """
        Return a list of points that enclose the given point in parameter, in function of the dimension of the point and the lambda_error
        """
        raise NotImplementedError

    def discretise_point_set(self, points):
        """
        Return a list of points that enclose all the given point in parameter, in function of the dimension of the point and the lambda_error
        """
        results = []
        for point in points:
            results += self.discretise_point(point)
        return results

    def discretise_point_to_insert (self, points):
        """
        Return a list of points dicretize to insert in the Bloom filter.
        """
        raise NotImplementedError


    def discretise_point_to_test(self, points):
        """
        Return a list of points dicretize to test in the Bloom filter.
        """
        raise NotImplementedError


