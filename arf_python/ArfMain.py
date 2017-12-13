## ----------------------------------------------------------------------------
# constant
from arf_python.ARF import ARF
from arf_python.DataVector import DataVector

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
    def __init__(self, dim=1, domain=1000, min_range_size=4, size=1000, path_file_feed = None, path_file_test = None):
        data_vector_feed = DataVector(dim, path_file_feed)
        data_vector_test = DataVector(dim, path_file_test)
        arf = ARF(dim, domain, min_range_size, size)