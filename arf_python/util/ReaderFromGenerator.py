# -----------------------------------------------------------------------------------------
# Import
import os
import pandas as pd
import numpy as np
from random import randint, uniform

from arf_python.util.DataProvider import DataProvider
from arf_python.Point import Point
from arf_python.Logger import Logger
# -----------------------------------------------------------------------------------------
# Constant

DATA_FOLDER = "../data"


# -----------------------------------------------------------------------------------------
# Code

logger = Logger("RandomDataGenerator")

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
    def __init__(self, dimension, size_of_data_set=1000, domain=10000, distribution=0):
        DataProvider.__init__(self, dimension)
        self.domain = domain
        self.distribution = distribution
        self.size_of_data_set = size_of_data_set

    def genarate(self, save_file_name=None):
        """
        This method genrate the data and store it into the object attribute point_list.
        :param save_file_name: name of the file in which we will store the generate data for next tests.
            if this parameter if not registered the data will be not save.
        :return: Nothing.
        """
        array_vector = np.random.randint(self.domain, size=(self.size_of_data_set, self.dimension))
        for vct in array_vector:
            self.point_list.append(Point(list(vct)))
        if save_file_name:
            try:
                os.remove(os.path.join(os.getcwd(), DATA_FOLDER, save_file_name))
            except OSError:
                pass
            vector_data_frame_ = pd.DataFrame(array_vector)
            vector_data_frame_.to_csv(os.path.join(os.getcwd(),DATA_FOLDER,save_file_name), encoding='utf-8')

    def genarate_similar(self, delta, data_set, save_file_name=None):
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
        number_of_test = 0
        array_vector = []
        while number_of_vector < self.size_of_data_set:
            index = randint(0, len(data_set)-1)
            vct = list(data_set[index].coordinates)
            for i in range(len(vct)):
                vct[i]+= uniform(0,1)*delta
            point = Point(vct)
            if point.distance(data_set[index]) < delta:
                self.point_list.append(point)
                array_vector.append(vct)
                number_of_vector += 1
            number_of_test += 1
            if number_of_test >= 1000*len(data_set):
                logger.error("infinit loop to construct similar")
                assert(False)
        if save_file_name:
            try:
                os.remove(os.path.join(os.getcwd(), DATA_FOLDER, save_file_name))
            except OSError:
                pass
            pd.DataFrame(array_vector).to_csv(os.path.join(os.getcwd(), DATA_FOLDER, save_file_name), encoding='utf-8')


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
        number_of_test = 0
        array_vector = []
        while number_of_vector < self.size_of_data_set:
            vct= np.random.randint(self.domain, size=(self.size_of_data_set, self.dimension)).tolist()[0]
            point = Point(vct)
            if self.distant_enough(point, delta, data_set):
                self.point_list.append(point)
                array_vector.append(vct)
                number_of_vector += 1
            number_of_test += 1
            if number_of_test >= 1000*len(data_set):
                logger.error("infinite loop to construct different")
                assert(False)

        if save_file_name:
            try:
                os.remove(os.path.join(os.getcwd(), DATA_FOLDER, save_file_name))
            except OSError:
                pass
            pd.DataFrame(array_vector).to_csv(os.path.join(os.getcwd(), DATA_FOLDER, save_file_name), encoding='utf-8')

        return array_vector

    # overrides(DataProvider)
    def get_points(self):
        """
        Provide the data in the forme of a list of Point objects
        """
        return self.point_list


# Do not read it, it is for the next iteration
# random.uniform(a, b)
# random.choice(seq)

