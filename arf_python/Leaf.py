# -------- Aim of the file

# This file provide an abstract class with method to frame a point

# -------- Import
from arf_python.GeneralNode import GeneralNode
# --------- Constants


# --------- Code
class Leaf(GeneralNode):
    """
    This class is an implementation of Dicretisator for a "rectangle" discrtisation.
    Args :
    :param lambda_error: float representing how each coordinates of the points should be ceil or floor.
    """

    def __init__(self, father, has_element = None):
        GeneralNode.__init__(self, father)
        self.has_element = has_element
        self.used = False

    def get_value(self):
        """
        return the value of the leaf.
        """
        return self.has_element

    def set_value(self, has_element_new):
        """
        Return a list of points dicretize to insert in the Bloom filter.
        """
        self.has_element = has_element_new

    def change_leaf_value(self, place, has_element_new):
        """
        Change the value of a leaf.
        """
        self.has_element = has_element_new

    def print_data(self):
        """
        Change the value of a leaf.
        """
        print("LEAF With value : " + str(self.has_element))
