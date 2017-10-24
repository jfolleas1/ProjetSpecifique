# -------- Aim of the file

# This file provide a class Point that will be our data strutur for the data that will fit our Bloom Filter

# -------- Import

import abc
from src.util.Logger import Logger
logger = Logger()



# --------- Constant


# --------- Code
class DataProvider:
    """
    This class is the interface for all data providers. The data provided will be use by the Bloom filter.
    Args :
    :param dimension: int that represent dimention of the vector that will be in the data.
    :param size_of_data_set: Size of the data set.
    """
    __metaclass__ = abc.ABCMeta


    def __init__(self, dimension, size_of_data_set):
        self.dimension = dimension
        self.size_of_data_set = size_of_data_set

    @abc.abstractmethod
    def get_points(self):
        """
        Provide the data in the forme of a list of Point objects
        """
        logger.error("call super method")
        return
