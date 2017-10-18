# -----------------------------------------------------------------------------------------
# Import
import DataProvider
from pathlib import Path
import DataProvider
# -----------------------------------------------------------------------------------------
# Constant
SEPARATOR_COORDINATE = " "

# -----------------------------------------------------------------------------------------
# Code
class ReaderFromFile(DataProvider):
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
    def __init__(self, dimension, repositoryPath ,fileName):
        DataProvider.__init__(dimension, 0)
        self.repositoryPath = repositoryPath
        self.fileName = fileName
        self.listPoints = []


    def Get_points(self):

        # We test if the file exist
        pathFile = Path(self.repositoryPath + self.fileName)
        if not pathFile.is_file():
            raise Exception("The file does not exist"+ str(pathFile))

        try:
            with open(pathFile) as file:
                line_counter = 0
                for line in file:
                    line_counter += 1
                    coodinates = line.split(SEPARATOR_COORDINATE)
                    if len(coodinates) != self.dimension:
                        raise Exception("The dimension of the point at line " + str(line_counter) + " is not correct")

        except Exception as e:
            print("Probleme during reading line " + str(line_counter))
            raise e





