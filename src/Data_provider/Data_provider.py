# -------- 
# Aim of the file

# This file provide a class Point that will be our data strutur for the data that will fit our Bloom Filter

# -------- 
# Import

from abc import ABCMeta, abstractmethod
import pandas as pd
import numpy as np


from src.Data_structur.Point import Point



# ---------
#  Constant


# --------- 
# Code


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
    
    @abstractmethod
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
    def __init__(self, dimension, size_of_data_set, domain, distribution=0, point_list=[]):
        DataProvider.__init__(self, dimension, size_of_data_set)
        self.domain = domain
        self.distribution = distribution
        self.point_list = point_list

    def genarate(self, save_file_name=None):
        """
        This method genrate the data and store it into the object attribute point_list.
        :param save_file_name: name of the file in which we will store the generate data for next tests.
            if this parameter if not registered the data will be not save.
        :return: Nothing.
        """
        array_vector = np.random.randint(self.domain, size=(self.size_of_data_set, self.dimension))
        for vct in array_vector:
            self.point_list.append(Point(self.dimension, vct))
        if save_file_name:
            vector_data_frame_ = pd.DataFrame(array_vector)
            vector_data_frame_.to_csv(save_file_name, encoding='utf-8')

    @staticmethod
    def distant_enough(point, delta, data_set):
        """
        This method verify that the point <point> is distant enough (at least <delta>) to all points in <data_set>.
        :param point: The point, as object Point, that want to insert to the generated data.
        :param delta: (float) the minimum distance between the point <point> to the <data_set>
        :param data_set: The data set in form of list of object Point
        :return: Boolean at True is the point <point> is at at least <delta> from all points in <data_set>
        """
        for other_point in data_set:
            if point.distance(other_point) <= delta:
                return False
        return True

    def genarate_falses(self, delta, data_set, save_file_name=None):
        """
        This method genrate the data and store it into the object attribute point_list. Each point generated in
            list_point is at least at <delta> from any point in <data_set>.
        :param delta: (float) the minimum distance between the point <point> to the <data_set>
        :param data_set: The data set in form of list of object Point
        :param save_file_name: name of the file in which we will store the generate data for next tests.
            if this parameter if not registered the data will be not save.
        :return: Nothing
        """
        number_of_vector = 0
        list_of_distant_vector = []
        while number_of_vector < self.size_of_data_set:
            vct= np.random.randint(self.domain, size=(self.size_of_data_set, self.dimension)).tolist()[0]
            point = Point(self.dimension, vct)
            if self.distant_enough(delta, data_set):
                self.point_list.append(point)
                if save_file_name:
                    list_of_distant_vector.append(vct)
                number_of_vector += 1
        if save_file_name:
            pd.DataFrame(list_of_distant_vector).to_csv(save_file_name, encoding='utf-8')

    def Get_points(self):
        """
        Provide the data in the forme of a list of Point objects
        """
        return self.point_list


# Do not read it, it is for the next iteration
# random.uniform(a, b)
# random.choice(seq)