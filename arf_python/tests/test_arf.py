import unittest

from arf_python.ARF import ARF
from arf_python.Point import Point

class RandomTest(unittest.TestCase):

    """Test on the ARF algorithm"""

    def test_arf1_pile(self):
        arf1 = ARF(dim=2, domain=32, min_range_size=4)
        arf1.insert_one_point(Point([3, 5]))
        res = arf1.test_one_point(Point([3, 5]))
        self.assertEqual(res, True, "ARF test exact same value")

    def test_arf1_almost(self):
        arf1 = ARF(dim=2, domain=32, min_range_size=4)
        arf1.insert_one_point(Point([3, 5]))
        res = arf1.test_one_point(Point([2, 6]))
        self.assertEqual(res, True, "ARF don't match on almost sames values")

    def test_arf1_domaine(self):
        arf1 = ARF(dim=2, domain=30, min_range_size=4)
        self.assertEqual(32, arf1.domain), "ARF don't have the correct domaine"

    def test_arf_mrs_1(self):
        arf1 = ARF(dim=2, domain=32, min_range_size=1)
        arf1.insert_one_point(Point([3, 5]))
        res = arf1.test_one_point(Point([3, 5]))
        self.assertEqual(res, True, "Problem with ARF with min range size = 1")

    def test_arf_set_test(self):
        arf1 = ARF(dim=2, domain=32, min_range_size=4)
        arf1.insert_one_point(Point([3, 5]))
        res = arf1.test_set_of_points([Point([3, 5]), Point([7, 12])])
        self.assertEqual(res, [True, False], "Problem with ARF with set of tests")

    def test_arf_collision(self):
        arf1 = ARF(dim=2, domain=32, min_range_size=4)
        arf1.insert_one_point(Point([3, 5]))
        arf1.insert_one_point(Point([3, 5]))
        res = arf1.test_one_point(Point([3, 5]))
        self.assertEqual(res, True, "Problem with ARF with collision inside inputs")

    def test_arf_dim4(self):
        arf1 = ARF(dim=4, domain=32, min_range_size=4)
        arf1.insert_one_point(Point([3, 5, 3, 5]))
        res = arf1.test_set_of_points([Point([3, 5, 3, 5]), Point([7, 12, 3, 5])])
        self.assertEqual(res, [True, False], "Problem with ARF dim = 4")

    def test_arf_dim3(self):
        arf1 = ARF(dim=3, domain=32, min_range_size=4)
        arf1.insert_one_point(Point([3, 5, 3]))
        res = arf1.test_set_of_points([Point([3, 5, 3]), Point([7, 12, 3])])
        self.assertEqual(res, [True, False], "Problem with ARF dim = 3")
