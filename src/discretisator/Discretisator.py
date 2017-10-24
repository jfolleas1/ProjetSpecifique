# -------- Aim of the file

# This file provide an abstract class with method to dicscretise a point

# -------- Import

from abc import ABCMeta, abstractmethod
from decimal import Decimal

# --------- Constant


# --------- Code
class Discretisator:
    """
    This class is the interface for all data discretisators.
    Args :
    :param lambda_error: float that represent dimention of the vector that will be in the data.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, lambda_error=0.01):
        self.lambda_error = Decimal(str(lambda_error))

    def discretise_point(self, point):
        raise NotImplementedError

    def discretise_point_set(self, points):
        """
        Provide the data in the forme of a list of Point objects
        """
        results = []
        for point in points:
            results += self.discretise_point(point)
        return results


