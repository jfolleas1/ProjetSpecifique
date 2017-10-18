# -------- Aim of the file

# This file provide a class Point that will be our data strutur for the data that will fit our Bloom Filter

# -------- Import

from abc import ABCMeta, abstractmethod
import pandas as pd
import numpy as np




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
    :param size_of_data_set: Size of the data set.
    :param domain: int that represent domain ([0,<domain>]) for dimension of the vectors that will be in the data.
    :param distribution: distribution of the random value:
        - 0 : uniform
        - x (10 > x >= 1): x normal laws superposed
    :param point_list: DataFrame that contain the data points:
    """
    def __init__(self, dimension, size_of_data_set, domain, distribution=0, point_list=pd.DataFrame()):
        DataProvider.__init__(self, dimension, size_of_data_set)
        self.domain = domain
        self.distribution = distribution
        self.point_list = point_list

    def Genarate(self, save_file_name=None):
        """
        This methode genrate the data and store it into the object attribute point_list.
        :param save_file_name: name of the file in which we will store the generate data for next tests.
            if this parameter if not registered the data will be not save.
        :return: Nothing.
        """
        self.point_list = pd.DataFrame(np.random.randint(self.domain, size=(self.size_of_data_set, self.dimension)))
        if save_file_name != None:
            self.point_list.to_csv(save_file_name, encoding='utf-8')

    def distant_enough(self, vector, delta, data_set):
    # TODO
        pass

    def Genarate_falses(self, delta, data_set, save_file_name=None):
        """
        This methode genrate the data and store it into the object attribute point_list.
        :param save_file_name: name of the file in which we will store the generate data for next tests.
            if this parameter if not registered the data will be not save.
        :return: Nothing.
        """
        number_of_vector = 0
        while number_of_vector < self.size_of_data_set:
            vct= np.random.randint(self.domain, size=(self.size_of_data_set, self.dimension)).tolist()
            if distant_enough(vct[0], delta, data_set):
                self.point_list.append(pd.DataFrame(vct))
                number_of_vector += 1
        if save_file_name != None:
            self.point_list.to_csv(save_file_name, encoding='utf-8')


# random.uniform(a, b)
# random.choice(seq)