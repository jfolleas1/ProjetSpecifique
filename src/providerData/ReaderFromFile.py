# -----------------------------------------------------------------------------------------
# Import
from src.providerData.DataProvider import DataProvider
from pathlib import Path
from src.structureData.Point import Point
from src.util.Logger import Logger
# -----------------------------------------------------------------------------------------
# Constant
SEPARATOR_COORDINATE = " "

# -----------------------------------------------------------------------------------------
# Code


class ReaderFromFile(DataProvider):
    """
    This class allow to provide data read from file.
    Args :
    :param dimension: int that represent dimention of the vector that will be in the data.
    TODO
    """
    def __init__(self, dimension, file_name):
        DataProvider.__init__(self, dimension, 0)
        self.file_name = file_name
        self.listPoints = []
        self.logger = Logger('ReaderFromFile')

    def get_points(self):
        # We test if the file exist
        path_file = Path(self.repository_path + self.file_name)
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
                    coodinates = line.split(SEPARATOR_COORDINATE)
                    if len(coodinates) != self.dimension:
                        self.logger.error('The dimension is not correct')
                        raise Exception("The dimension of the point at line " + str(line_counter) + " is not correct")
                    self.listPoints.append(Point(coodinates))

        except Exception as e:
            self.logger.error("Probleme during reading line " + str(line_counter))
            raise e

        return self.listPoints