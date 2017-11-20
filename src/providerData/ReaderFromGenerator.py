# -----------------------------------------------------------------------------------------
# Import
import os
import pandas as pd
import numpy as np
from src.providerData.DataProvider import DataProvider
from src.structureData.Point import Point
from src.util.Logger import Logger
from copy import deepcopy
import random

# -----------------------------------------------------------------------------------------
# Constant

DATA_FOLDER = "../../data"

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
        print("IN CONST : " + str(len(self.point_list)))
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
            vector_data_frame_ = pd.DataFrame(array_vector)
            vector_data_frame_.to_csv(os.path.join(os.getcwd(), DATA_FOLDER, save_file_name), encoding='utf-8')

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
            if point.distance(other_point) < delta:
                return False
        return True

    def genarate_positives(self, delta, data_set, save_file_name=None):
        """
        This method genrate the data and store it into the object attribute point_list. Each point generated in
            list_point is at the most at <delta> from a point in <data_set>.
        :param delta: (float) the maximum distance between the point <point> to the <data_set>
        :param data_set: The data set in form of list of object Point
        :param save_file_name: name of the file in which we will store the generate data for next tests.
            if this parameter if not registered the data will be not save.
        :return: Nothing
        """
        number_of_vector = 0
        number_of_test = 0
        array_vector = []
        while number_of_vector < self.size_of_data_set:
            vect = deepcopy(data_set[number_of_test % len(data_set)])
            vect.coordinates[0] += int(random.uniform(-1, 1) * delta)
            if not self.distant_enough(vect, delta, data_set):
                self.point_list.append(vect)
                array_vector.append(vect.coordinates)
                number_of_vector += 1
            number_of_test += 1
            if number_of_test >= 1000 * len(data_set):
                logger.error("infinit loop to construct different")
                assert (False)
        if save_file_name:
            pd.DataFrame(array_vector).to_csv(os.path.join(os.getcwd(), DATA_FOLDER, save_file_name), encoding='utf-8')

    def genarate_falses_domain(self, delta, data_set, save_file_name=None):
        points = []
        f_results = []

        if self.dimension>1:
            for i in range(0, self.domain):
                points.append([i])
            self.genarate_falses_domain_rec(1, points, delta, data_set, f_results)
        else:
            for i in range(0, self.domain):
                point_obj = Point([i])
                if self.distant_enough(point_obj, delta, data_set):
                    f_results.append(point_obj)
        self.point_list = f_results



    def genarate_falses_domain_rec(self, start, points, delta, data_set, f_results):
        if start < self.dimension:
            results = []
            for i in range(0, len(points)):
                point_i_c = deepcopy(points[i])
                for k in range(0, self.domain):
                    p = point_i_c + [k]
                    point_obj= Point(p)
                    if start == self.dimension - 1:
                        if self.distant_enough(point_obj, delta, data_set):
                            f_results.append(point_obj)
                    else:
                        results.append(p)
                        self.genarate_falses_domain_rec(start + 1, results, delta, data_set, f_results)

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
            vct = np.random.randint(self.domain, size=self.dimension)
            vct = vct.tolist()
            point = Point(vct)
            if self.distant_enough(point, delta, data_set):
                self.point_list.append(point)
                array_vector.append(vct)
                number_of_vector += 1
            number_of_test += 1
            if number_of_test >= 1000 * len(data_set):
                logger.error("infinit loop to construct different")
                assert (False)
        if save_file_name:
            pd.DataFrame(array_vector).to_csv(os.path.join(os.getcwd(), DATA_FOLDER, save_file_name), encoding='utf-8')

    # overrides(DataProvider)
    def get_points(self):

        """
        Provide the data in the forme of a list of Point objects
        """
        return self.point_list

# Do not read it, it is for the next iteration
# random.uniform(a, b)
# random.choice(seq)

