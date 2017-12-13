## ----------------------------------------------------------------------------
# constant
from arf_python.ARF import ARF
from arf_python.DataVector import DataVector
from arf_python.util.Constant import Constant
from arf_python.util.RectangleDiscretisator import RectangleDiscretisator
## ----------------------------------------------------------------------------
# constant

## ----------------------------------------------------------------------------
# code


# --------- Code
class ArfMAin:
    """
    This class is a simple implementation of the ARF. It is not suppose to be a scalable implementation.
    Args :
    :param dim: int that represent the dimension of the vector space.
    :param domain: int that represent the domain of the vector space.
    :param size: int that is the size of the ARF in bits.
    """
    def __init__(self, path_file_feed, path_file_test, dim=1, domain=1000, min_range_size=4, size=1000):
        # get data for feed
        self.data_vector_feed = DataVector(dim, path_file_feed)
        # get data for test
        self.data_vector_test = DataVector(dim, path_file_test)
        self.arf = ARF(dim, domain, min_range_size, size)


    def feed(self, discretize_param = Constant.DIS_TESTS, discretizator = None):

        pass

    def test(self, discretize_param = Constant.DIS_TESTS, discretizator = None):
        pass