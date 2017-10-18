# -----------------------------------------------------------------------------------------
# Import
import pandas as pd
import numpy as np
from src.providerData.DataProvider import DataProvider
from src.structureData.Point import Point
# -----------------------------------------------------------------------------------------
# Constant


# -----------------------------------------------------------------------------------------
# Code
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
        for other_point in data_set:
            if point.distance(other_point) <= delta:
                return False
        return True

    def genarate_falses(self, delta, data_set, save_file_name=None):
        """
        This methode genrate the data and store it into the object attribute point_list.
        :param save_file_name: name of the file in which we will store the generate data for next tests.
            if this parameter if not registered the data will be not save.
        :return: Nothing.
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

