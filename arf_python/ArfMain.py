## ----------------------------------------------------------------------------
# constant
from arf_python.ARF import ARF
from arf_python.DataVector import DataVector
import arf_python.util.Constants as Constants
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
    def __init__(self, path_file_feed, path_file_test, dim=1, domain=1000, size=1000, delta_error=1,
                 methode_discretize = Constants.DIS_TESTS):
        self.discretizor = RectangleDiscretisator(delta_error, methode_discretize)
        # get data for feed
        self.data_vector_feed = DataVector(dim, path_file_feed)
        # get data for test
        self.data_vector_test = DataVector(dim, path_file_test)
        if methode_discretize == Constants.DIS_DOUBLE:
            min_range_size = delta_error
        else:
            min_range_size = 2*delta_error
        self.arf = ARF(dim, domain, min_range_size, size)


    def feed(self):
        """

        :return:
        """
        points = self.data_vector_feed.get_points()
        d_points = self.discretizor.discretise_points_to_insert(points)
        self.arf.insert_set_of_points(d_points)

    def test(self):
        """
        :return:
        """
        points = self.data_vector_feed.get_points()
        d_points = self.discretizor.discretise_points_to_test(points)
        return self.arf.test_set_of_points(d_points)
