# -------- Aim of the file

# This file provide an abstract class with method to frame a point

# -------- Import
from arf_python.GeneralNode import GeneralNode
from copy import deepcopy
from arf_python.Logger import Logger
from arf_python.Leaf import Leaf
import math
# --------- Constants


# --------- Code
class Node(GeneralNode):
    """
    This class is an implementation of Dicretisator for a "rectangle" discrtisation.
    Args :
    :param lambda_error: float representing how each coordinates of the points should be ceil or floor.
    """


    # Static variable of class.
    dim = 1
    min_range_size = 1
    deep = 0
    logger = Logger('Node')

    # deep copy
    def __init__(self, father = None, my_node = None):
        if  my_node != None:
            node_deep = deepcopy(my_node)
            GeneralNode.__init__(self, node_deep.father)
            self.children_nodes = node_deep.child_nodes
            self.children_leaf = node_deep.childs_are_leaf

        else:
            GeneralNode.__init__(self, father)
            # initiatiate Node
            self.children_nodes = {}

            # initiate leaves, we begin with all leaf and False value for has_element parameter.
            self.children_leaf = {}
            for place in range(int(math.pow(2, Node.dim))):
                self.children_leaf[place] = Leaf(self, False)


    def change_leaf_value(self, place, has_element_new):
        """
        Change the value of a leaf.
        """
        # There is no leaf
        if not place in self.children_leaf:
            Node.logger.error("try to update a inexistent leaf")
            raise Exception("There is no leaf at this place")
        # We change the value contained at the place.
        else:
            self.children_leaf[place].change_leaf_value(None, has_element_new)

    # the leaf become a node
    def split(self, place_leaf_splitted):
        """
        the leaf become a node.
        """
        self.children_leaf = _remove_key(self.children_leaf, place_leaf_splitted)
        self.children_nodes[place_leaf_splitted] = Node(self)

    def son_is_leaf(self, place):
        """
        Test if the son of a node is a leaf.
        """
        return place in self.children_leaf

    def only_got_leaves_child (self):
        """
        Test if the current node has only leaves as children
        :return:
        """
        if len(self.children_nodes) == 0:
            return True

        return False

    def leaves_got_same_value(self):
        """
        Test if all leaves have the same values
        :return:
        """
        # check if the nodes has some leaves
        if len(self.children_nodes) > 1:
            Node.logger.warn("Current nodes have nodes as children")

        first_has_element = self.children_leaf[list(self.children_leaf)[0]].get_value()

        # Loop on leaves in order to check if every leaves has the same values.
        for place, leaf in self.children_leaf.items():
            if leaf.get_value() != first_has_element:
                return False

        return True

    def change_child_value(self, child_ref, hasElement):
        """
        Change the value of the current Node or Leaf indicated by child_ref
        the new value is a Leaf with the value = hasElement
        :param child_ref:
        :param hasElement:
        :return:
        """
        place_changement = None
        # if it is a node, we remove it and insert a leaf
        for place, node  in self.children_nodes.items():
            if node == child_ref:
                self.children_nodes = _remove_key(self.children_nodes, place)
                self.children_leaf[place] = Leaf(self, hasElement)
                place_changement = place
                break

        # if it is a leaf we only change the value
        for place, leaf in self.children_leaf.items():
            if leaf == child_ref:
                self.change_leaf_value(place, hasElement)
                place_changement = place


        # We return the leaf if and only if we have change the value.
        if place_changement == None:
            return None

        return self.children_leaf[place_changement]

    def get_child_node (self, place):
        """
        Get the Node or Leaf at the indicated place
        :param place:
        :return:
        """
        if place in self.children_nodes:
            return self.children_nodes[place]
        elif place in self.children_leaf:
            return self.children_leaf[place]
        else:
            Node.logger.error("Error, there is no Node in the place " + str(place))

    def merge(self):
        """
        Change the node in leaf and modify the father value.
        :return: the created leaf
        """

        # check if the nodes has some leaves
        if len(self.children_nodes) > 1:
            Node.logger.warn("Current nodes have nodes as children")

        # Compute the value with different values.
        leaf_value = False
        for place, leaf in self.children_leaf.items():
            leaf_value |= leaf.get_value()

        # Change the value of the father and put leaves instead.
        return self.father.change_child_value(self, leaf_value)

    def had_useful_leaves(self, min):
        """
        Reduce the number of leaf used byut the ARF if it is needed.
        :param min:
        :return:
        """
        number_useful_leaves = 0
        # Count number of leaves used.
        for place, leaf in self.children_leaf.items():
            if leaf.used:
                number_useful_leaves += 1

        # The number of useful Leaves if superior to
        if number_useful_leaves > min:
            for place, leaf in self.children_leaf.items():
                leaf.used = False

            return True

        return False

    def add_nodes(self, nodes):
        """
        add nodes to the father
        :param min:
        :return:
        """
        self.children_nodes = nodes

    def add_leaves(self, leaves):
        """
        add nodes to the father
        :param min:
        :return:
        """
        self.children_leaf = leaves

    def print_data(self):
        Node.deep += 1
        print ( "NODE ---------------------------------------")
        for place, leaf in self.children_leaf.items():
            print("     place = "+ str(place) +" leaf value = " + str(leaf.get_value()))

        for place, node in self.children_nodes.items():
            print("place :"+ str(place) +" Node deep :" + str(Node.deep))
            node.print_data()

        Node.deep -= 1

    def get_leaves(self):
        """
        :return: the leaves children
        """
        return self.children_leaf

#---------------------------------------------------------------------------------------------------------------

# Public
def set_dim(new_dim):
    """
    Change the dimension value
    :param new_dim:
    :return:
    """
    Node.dim = new_dim

def set_min_range_size(new_min_range_size):
    """
    Change the min range size value.
    :param new_min_range_size:
    :return:
    """
    Node.min_range_size = new_min_range_size


# -----------------------------------------------------------------------------------------
# Private methods
def _remove_key(d, key):
    """
    remove properly a key of a dict and return the new reference.
    :param d:
    :param key:
    :return:
    """
    r = dict(d)
    del r[key]
    return r