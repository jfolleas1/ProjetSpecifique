# -------- Aim of the file

# This file provide an the call ARF of the implementation of the ARF

# -------- Import
import copy
import time

from arf_python.Leaf import Leaf
from arf_python.Node import Node
from arf_python.Point import Point
from arf_python.util.ReaderFromGenerator import RandomDataGenerator
# --------- Constants


# --------- Code
class ARF:
    """
    This class is a simple implementation of the ARF. It is not suppose to be a scalable implementation.
    Args :
    :param dim: int that represent the dimension of the vector space.
    :param domain: int that represent the domain of the vector space.
    :param size: int that is the size of the ARF in bits.
    """
    def __init__(self, dim=1, domain=1000, min_range_size=4, size=1000):
        def get_real_domain(input_domain, min_range_size):
            real_domain = min_range_size
            while real_domain<input_domain:
                real_domain*=2
            return real_domain
        self.dim = dim
        self.min_range_size = min_range_size
        self.domain = get_real_domain(domain, min_range_size)
        self.expected_size_in_bits = size
        # Set the Node class attributs
        Node.dim = dim
        Node.min_range_size = min_range_size
        self.root = Node(None) # root GeneralNode, is the only one with no father
        self.list_of_leaves_and_depth = {} # List of tuple (leaf, depth); will help for erase the tree
        for ind in range(2**self.dim):
            self.list_of_leaves_and_depth[self.root.get_child_node(ind).__repr__()] = (self.root.get_child_node(ind), 1)
        self.real_size_nodes = 5

    def __get_max_depth(self):
        max_depth = 0
        doamin_cpy = self.domain
        while doamin_cpy % 2 == 0:
            doamin_cpy/=2
            max_depth+=1
        return max_depth

    def get_bit_size(self):
        return (2**self.dim)*(self.real_size_nodes - len(self.list_of_leaves_and_depth.values())) + \
               len(self.list_of_leaves_and_depth.values())

    def __get_num_of_son_and_new_middle(self, point, middle, domain_of_current_node):
        assert type(point) == Point, ":param middle: must be a Point"
        assert type(middle) == list, ":param middle: must be a list"
        assert len(middle) == self.dim, ":param middle: must have the same dimension than the ARF"
        assert point.dimension == self.dim, ":param point: must be of the same dimension than the ARF"
        assert (2*domain_of_current_node)%2 == 0, ":param domain_of_current_node: is not span"
        num_of_son = 0
        new_middle = copy.deepcopy(middle)
        for i in range(len(point.coordinates)):
            if point.coordinates[i] >= middle[i]:
                num_of_son += 2**i
                new_middle[i] += (domain_of_current_node/2)
            else:
                new_middle[i] -= (domain_of_current_node/2)
        return num_of_son, new_middle

    def __move_to_the_next_node(self, point, middle, current_node, domain_of_current_node):
        assert type(point) == Point, ":param point: must be a Point"
        assert type(middle) == list, ":param middle: must be a list"
        assert len(middle) == self.dim, ":param middle: must have the same dimension than the ARF"
        assert point.dimension == self.dim, ":param point: must be of the same dimension than the ARF"
        assert type(current_node) == Node, "Leaves have no sons"
        num_of_son, new_middle = self.__get_num_of_son_and_new_middle(point, middle, domain_of_current_node)

        new_GNode = current_node.get_child_node(num_of_son)
        return new_GNode, new_middle

    def __get_corresponding_leaf(self, point):
        assert type(point) == Point, ":param point: must be a Point"
        assert point.dimension == self.dim, ":param point: must be of the same dimension than the ARF"
        current_middle = [self.domain/2]*self.dim
        current_node = self.root
        domain_of_current_node = self.domain/2
        depth = 0
        prev_middle = None
        while type(current_node) != Leaf:
            prev_middle = copy.deepcopy(current_middle)
            current_node, current_middle = self.__move_to_the_next_node(point, current_middle, current_node,
                                                                      domain_of_current_node)
            domain_of_current_node /= 2
            depth += 1

            assert 2*domain_of_current_node / self.min_range_size >= 1, "To deep tree, :domain_of_current_node: must" \
                                                                    " be a multiple of :min_range_size:"
        return current_node, depth, prev_middle

    def get_corresponding_leaf(self, point):
        return self.__get_corresponding_leaf(point)

    def test_one_point(self, point):
        """
        Test one point with the filter
        :param point: the point we want to test, must be a Point of same dimension than the ARF
        :return: Boolean at True is the answer is yes.
        """
        assert type(point) == Point, ":param point: must be a Point"
        assert point.dimension == self.dim, ":param point: must be of the same dimension than the ARF"
        corresponding_leaf, _, _ = self.__get_corresponding_leaf(point)
        return corresponding_leaf.get_value()

    def test_set_of_points(self, set_of_points):
        """
        Test a set of points with the filter
        :param set_of_points: the points we want to test, must be a list of Point of same dimension than the ARF
        :return: list of Boolean at True is the answer for the corresponding point is yes.
        """
        list_of_answer = []
        for point in set_of_points:
            list_of_answer.append(self.test_one_point(point))
        return list_of_answer

    def insert_one_point(self, point):
        """
        Instert one point in the filter
        :param point: the point we want to test, must be a Point of same dimension than the ARF
        :return: Nothing
        """
        assert type(point) == Point, ":param point: must be a Point"
        assert point.dimension == self.dim, ":param point: must be of the same dimension than the ARF"
        current_leaf, current_depth, current_middle = self.__get_corresponding_leaf(point)
        assert current_depth > 0, "The ARF root must be a node"
        current_domain = self.domain/2**current_depth
        min_range_size = self.min_range_size

        while current_domain > min_range_size:
            current_domain /= 2

            num_of_son, current_middle = self.__get_num_of_son_and_new_middle(point, current_middle, 2*current_domain)
            father_of_leaf = current_leaf.get_father()
            depth_of_next_leaf = self.list_of_leaves_and_depth[current_leaf.__repr__()][1]+1 # update liste of leaves
            del self.list_of_leaves_and_depth[current_leaf.__repr__()] # update liste of leaves
            father_of_leaf.split(num_of_son)
            self.real_size_nodes += 2 ** self.dim
            father_of_leaf = father_of_leaf.get_child_node(num_of_son)
            for ind in range(2**self.dim): # update liste of leaves
                self.list_of_leaves_and_depth[father_of_leaf.get_child_node(ind).__repr__()] = \
                    (father_of_leaf.get_child_node(ind), depth_of_next_leaf) # update liste of leaves
            current_leaf, _ = self.__move_to_the_next_node(point, current_middle, father_of_leaf, current_domain)
        current_leaf.set_value(True)

    def insert_set_of_points(self, points):
        """
        Instert all point of a set in the filter
        :param point: the point we want to test, must be a Point of same dimension than the ARF
        :return: Nothing
        """
        assert type(points) == list, ":param points: must be a list of Point"
        assert type(points[0]) == Point, ":param points: must be a list of Point"
        assert points[0].dimension == self.dim, ":param points: must a list of point which have " \
                                                "the same dimension than the ARF"
        for point in points:
            self.insert_one_point(point)


    def __merge_one_node(self, node):
        """

        :param node: node to merge (not a leaf)
        :return: Nothing
        """
        depth = self.list_of_leaves_and_depth[node.get_child_node(0).__repr__()][1]-1
        for ind in range(2**self.dim):
            del self.list_of_leaves_and_depth[node.get_child_node(ind).__repr__()]
        leaf = node.merge()
        self.list_of_leaves_and_depth[leaf.__repr__()] = (leaf, depth)

    def __erase_unusfull_leaves(self):
        """
        TODO
        :return:
        """
        no_changes = False
        while not no_changes:
            no_changes = True
            for leaf, _ in self.list_of_leaves_and_depth.values():
                if leaf.father.only_got_leaves_child():
                    if leaf.father.leaves_got_same_value():
                        if leaf.father != self.root:
                            self.__merge_one_node(leaf.father)
                            no_changes = False
                            break


    def __erase_deepest_leaves(self):
        """
        TODO
        :return: Nothing
        """
        while self.get_bit_size() > self.expected_size_in_bits:
            #take all the deepest leaves
            deepest_level = max(list(map(lambda x: x[1], self.list_of_leaves_and_depth.values())))
            deepest_leaves = list(map(lambda x: x[0], filter(lambda x: x[1] == deepest_level,
                                                        self.list_of_leaves_and_depth.values())))
            list_of_father_to_merge = []
            for leaf in deepest_leaves:
                if leaf.father not in list_of_father_to_merge and leaf.father.only_got_leaves_child():
                    list_of_father_to_merge.append(leaf.father)
            for father in list_of_father_to_merge:
                if self.get_bit_size() > self.expected_size_in_bits:
                    self.__merge_one_node(father)
                    self.real_size_nodes -= 2 ** self.dim
                else:
                    break

    def erase(self):
        # first round
        self.__erase_unusfull_leaves()
        self.__erase_deepest_leaves()


    #TODO Split it into one private function and one public with no args
    def __print(self, cur_node, cur_range, cur_range_size,cur_middle, depth):
        """
        Allow to print all the nodes which compose the ARF
        :return:
        """
        def compute_next_middles(cur_middle, list_of_building_middle, domain_of_cur_middle):
            if len(list_of_building_middle) < (2 ** len(cur_middle)):
                l1 = copy.deepcopy(list_of_building_middle)
                for i in range(len(list_of_building_middle)):
                    l1[i].append((cur_middle[len(l1[i])] + domain_of_cur_middle / 4))
                l2 = copy.deepcopy(list_of_building_middle)
                for i in range(len(list_of_building_middle)):
                    l2[i].append((cur_middle[len(l2[i])] - domain_of_cur_middle / 4))
                return compute_next_middles(cur_middle, l1 + l2, domain_of_cur_middle)
            else:
                return list_of_building_middle

        if type(cur_node) == Node:
            indentation = "\t"*depth
            print(indentation + "N " + cur_node.__repr__() + str(cur_range))
            next_middles = compute_next_middles(cur_middle, [[]], cur_range_size)
            next_ranges = list(map(lambda x: list(map(lambda y: [y-cur_range_size/4, y+cur_range_size/4], x)),
                                    next_middles))
            next_range_size = cur_range_size/2
            for i in range(len(next_ranges)):
                next_node, _ = self.__move_to_the_next_node(Point(next_middles[i]), cur_middle, cur_node, cur_range_size)
                self.__print(next_node, next_ranges[i], next_range_size, next_middles[i], depth+1)
        elif type(cur_node) == Leaf:
            # It's a leaf
            indentation = "\t" * depth
            if cur_node.get_value() == True:
                print(indentation + "L " + cur_node.__repr__() + str(cur_range) +  " *")
            else:
                print(indentation + "L " + cur_node.__repr__() + str(cur_range))

    def print(self):
        """
        Allow to print all the nodes which compose the ARF
        :return:
        """
        cur_range_size = self.domain
        cur_middle = [self.domain/2]*self.dim
        cur_range =[[0,self.domain]]*self.dim
        cur_node = self.root
        self.__print(cur_node, cur_range, cur_range_size, cur_middle,0)
        print("ROOT")






