# -------- Import
from arf_python.Logger import Logger
from arf_python.Point import Point
from decimal import *
import pandas as pd
from pathlib import Path
import math
import os


# --------- Constants
SEPARATOR_COORDINATE = ","

# --------- Code
class DataVector:

    logger = Logger("DataVector")

    def __init__(self, dimension,  file_path, points_list = [], size_of_data = 0):
        self.dimension = dimension
        self.size_of_data = size_of_data
        self.points_list = points_list

        # load data from file_path
        # initiate point_list and size_data
        if file_path != None:
            self.load_data(file_path)

    def load_data(self, file_path):
        """
        Load the data contained in file_path, file_path is a csv generated by pandas method to_csv.
        :param file_path:
        :return:
        """
        # We test if the file exist

        print(os.getcwd())
        self.points_list = []
        path_file = Path(file_path)
        DataVector.logger.info('We get the points from ' + str(path_file))

        if not path_file.is_file():
            DataVector.logger.error('The file does not exist')
            raise Exception("The file does not exist "+ str(path_file))

        data_file = pd.read_csv(str(path_file))
        line_counter = -1
        try:
            for i, row in enumerate(data_file.values):
                line_counter += 1
                coodinates = [Decimal(int(elem)) for index, elem in enumerate(row) if index != 0]

                # We get a dimension problem.
                if len(coodinates)!= self.dimension:
                    DataVector.logger.error('The dimension is not correct, expected : '+ str(len(coodinates)) + str(self.dimension))
                    raise Exception("The dimension of the point at line " + str(line_counter) + " is not correct")
                self.points_list.append(Point(coodinates))

            self.size_of_data = len(self.points_list)

        except Exception as e:
            DataVector.logger.error("Probleme during reading line " + str(line_counter))
            raise e

    def get_points(self):
        """
        Return the point list.
        :param file_path:
        :return:
        """
        return self.points_list

    def get_size_of_data(self):
        """
        Return the size of data.
        :param file_path:
        :return:
        """
        return self.size_of_data


