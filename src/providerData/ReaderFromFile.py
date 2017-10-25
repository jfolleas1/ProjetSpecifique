# -----------------------------------------------------------------------------------------
# Import
from src.providerData.DataProvider import DataProvider
from pathlib import Path
from src.structureData.Point import Point
from src.util.Logger import Logger
from decimal import *
# -----------------------------------------------------------------------------------------
# Constant
SEPARATOR_COORDINATE = ","

# -----------------------------------------------------------------------------------------
# Code


class ReaderFromFile(DataProvider):
    """
    This class allow to provide data read from file.
    Args :
    :param dimension: int that represent dimention of the vector that will be in the data.
    :param file_name: Name of file containing the data.
    """
    def __init__(self, dimension, file_path):
        DataProvider.__init__(self, dimension, [])
        self.file_path = file_path
        self.logger = Logger('ReaderFromFile')

    #@overrides(DataProvider)
    def get_points(self):
        # We test if the file exist
        path_file = Path(self.file_path)
        self.logger.info('We get the points from' + str(path_file))

        if not path_file.is_file():
            self.logger.error('The file does not exist')
            raise Exception("The file does not exist"+ str(path_file))

        line_counter = 0
        try:
            with open(str(path_file)) as file:
                for line in file:
                    line_counter += 1
                    line = line.replace('\n', '')
                    coodinates = [Decimal(elem) for elem in line.split(SEPARATOR_COORDINATE)]

                    # We get a dimension problem.
                    if len(coodinates)!= self.dimension:
                        self.logger.error('The dimension is not correct, expected : '+ str(len(coodinates)) + str(self.dimension))
                        raise Exception("The dimension of the point at line " + str(line_counter) + " is not correct")
                    self.point_list.append(Point(coodinates))

        except Exception as e:
            self.logger.error("Probleme during reading line " + str(line_counter))
            raise e

        return self.point_list