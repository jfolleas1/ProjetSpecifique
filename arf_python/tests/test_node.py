## ----------------------------------------------------------------------------
# Import
import unittest
from arf_python.Leaf import Leaf
from arf_python.Node import Node
import math
## ----------------------------------------------------------------------------

class RandomTest(unittest.TestCase):

    def setUp(self):
        root_test = Node()
        self.root = Node()
        self.node1 = Node(self.root)
        self.node2 = Node(self.root)
        self.leaves1 = {0: Leaf(self.node1, False), 1: Leaf(self.node1, False), 2: Leaf(self.node1, False), 3: Leaf(self.node1, False)}
        self.leaves2 = {0: Leaf(self.node2, True), 1: Leaf(self.node2, True), 2: Leaf(self.node2, False), 3: Leaf(self.node2, True)}
        self.leaves_root = {0: Leaf(self.root, True), 2: Leaf(self.node2, True)}
        self.nodes_root = {1: self.node1, 3: self.node2}

        self.node1.add_leaves(self.leaves1)
        self.node2.add_leaves(self.leaves2)
        self.root.add_nodes(self.nodes_root)
        self.root.add_leaves(self.leaves_root)

    def test_get_child_node(self):
        self.assertEqual(self.root.get_child_node(2), self.leaves_root[2], "Leaf are not equal")
        self.assertEqual(self.root.get_child_node(3), self.nodes_root[3], "Leaf are not equal")

    def test_get_child_node(self):
        self.node1.merge()
        self.assertEqual(self.root.get_child_node(1).get_value(), False, "Merge fail")

        self.node2.merge()
        self.assertEqual(self.root.get_child_node(3).get_value(), True, "Merge fail")

    def test_get_father(self):
        self.assertEqual(self.node1.get_father(), self.root, "get father fail")

    def test_son_is_leaf(self):
        self.assertEqual(self.root.son_is_leaf(1), False, "son is leaf")
        self.assertEqual(self.root.son_is_leaf(0), True, "son is leaf")

    def test_only_got_leaves_child(self):
        self.assertEqual(self.root.only_got_leaves_child(), False, "only  got child fail")
        self.assertEqual(self.node1.only_got_leaves_child(), True, "only  got child fail")

    def test_split(self):
        self.root.split(2)
        self.assertEqual(self.root.get_child_node(2).only_got_leaves_child(), True, "split fail")
        self.assertEqual(self.root.get_child_node(2).get_child_node(2).get_value(), False, "split fail")
        self.assertEqual(self.root.get_child_node(2).leaves_got_same_value(), True, "have the same value fail")

    def dim(self):
        Node.dim = 3
        root_test = Node ()
        self.assertEqual(len(root_test.get_leaves()), math.pow(2,3), "have the same value fail")
        self.assertEqual(root_test.get_child_node(2).get_value(), False, "split fail")
        self.assertEqual(root_test.leaves_got_same_value(), True, "have the same value fail")

        Node.dim = 4
        root_test = Node ()
        self.assertEqual(len(root_test.get_leaves()), math.pow(2,4), "have the same value fail")
        self.assertEqual(root_test.get_child_node(2).get_value(), False, "split fail")
        self.assertEqual(root_test.leaves_got_same_value(), True, "have the same value fail")

