# -------- Aim of the file

# This file provide a class Point that will be our data strutur for the data that will fit our Bloom Filter

# -------- Import

from abc import ABCMeta, abstractmethod
import random


# --------- Constant


# --------- Code


class DataProvider:
    """
    This class is the interface for all data providers. The data provided will be use by the Bloom filter.
    Args :
    :param dimension: int that represent dimention of the vector that will be in the data.
    :param size_of_data_set: Size of the data set.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, dimension, size_of_data_set):
        self.dimension = dimension
        self.size_of_data_set = size_of_data_set

    def Get_points(self):
        """
        Provide the data in the forme of a list of Point objects
        """
        pass


class RandomDataGenerator(DataProvider):
    """
    This class allow to provide data randomly.
    Args :
    :param dimension: int that represent dimention of the vector that will be in the data.
    :param domain: int that represent domain ([0,<domain>]) for dimension of the vectors that will be in the data.
    :param distibusion: distribution of the random value:
        - 0 : uniform
        - x (10 > x >= 1): x normal laws superposed
    :param size_of_data_set: Size of the data set.
    """
    def __init__(self, dimension, domain, distibusion=0):
        self.dimenstion = dimenstion
        self.domain = domain
        self.distibutions = distibutions
        self.size_of_data_set = size_of_data_set
        self.point_list = []

    def Genarate(self, save_file_name=None):
        """
        This methode genrate the data and store it into the object attribute point_list.
        :param save_file_name: name of the file in which we will store the generate data for next tests.
            if this parameter if not registered the data will be not save.
        :return: Nothing.
        """

# random.normalvariate
# random.uniform(a, b)
# random.choice(seq)