# -------- Aim of the file

# This file provide an abstract class with method to dicscretise a point

# -------- Import

from abc import ABCMeta, abstractmethod

# --------- Constant


# --------- Code
class GeneralNode:
    """
    This class is the interface for all data discretisators.
    Args :
    :param lambda_error: float representing how each coordinates of the points should be ceil or floor.
    """
    __metaclass__ = ABCMeta

    def __init__(self, father = None):
        self.father = father

    def get_father (self):
        """
        return the father of the leaf.
        :return:
        """
        return self.father

    @abstractmethod
    def get_value(self):
        """
        return the value of the leaf.
        """
        raise NotImplementedError

    @abstractmethod
    def set_value (self):
        """
        Return a list of points dicretize to insert in the Bloom filter.
        """
        raise NotImplementedError

    @abstractmethod
    def change_child_value(self, place, hasElement ):
        """
        Change the value of a child
        """
        raise NotImplementedError

    @abstractmethod
    def change_leaf_value(self, general_node, hasElement):
        """
        Change the value of a leaf.
        """
        raise NotImplementedError

    @abstractmethod
    def split(self, place_leaf_splitted):
        """
        The leaf become a node.
        """
        raise NotImplementedError

    @abstractmethod
    def son_is_leaf(self, place):
        """
        Teste if the son of a node is a leaf.
        """
        raise NotImplementedError

    @abstractmethod
    def print_data(place):
        """
        Teste if the son of a node is a leaf.
        """
        raise NotImplementedError