# -----------------------------------------------------------------------------------------
# Import

import math
from bloom_filter import BloomFilter

from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
from src.structureData.Point import Point

# -----------------------------------------------------------------------------------------
# Constant

# -----------------------------------------------------------------------------------------
# Code


class BloomFilterTester:
    """
    This class allow to create a Bloom filter with a fixed size and test his false positive rate.
    """

    def __init__(self, n, m, point_build=[], discretisator=None):
        """
        :param n: number of element that will be stored.
        :param m: size of the bloom filter in bit.
        :param point_build: list of object points to insert in the bloom filter
        """
        error_rate = float(math.exp((math.log(2) ** 2)*float(m)/float(-1*n)))
        self.bloom_filter = BloomFilter(n,error_rate)
        # TODO version with the choose of the Hash : the third parameter is the hash
        self.point_build = point_build
        if discretisator:
            for pt in point_build:
                for d_pt in discretisator.discretise_point(pt):
                    self.bloom_filter.add(d_pt.to_string())
        else:
            for pt in point_build:
                self.bloom_filter.add(pt.to_string())

    def _get_bf_size(self):
        """

        :return: The size of the bloom filter
        """
        return self.bloom_filter.num_bits_m

    def feed(self, points, discretisator=None):
        """
        Add all the points (discretizate if :discretisator: is not None) in the Bloom Filter
        :param points: the points that we want to index
        :param discretisator: the Discretizator that we will use to index data
        :return: Nothing
        """
        if discretisator:
            for pt in points:
                print("UPER LOOP : " + pt.to_string())
                for d_pt in discretisator.discretise_point(pt):
                    print(d_pt.to_string())
                    self.bloom_filter.add(d_pt.to_string())
        else:
            for pt in points:
                self.bloom_filter.add(pt.to_string())
        self.point_build += points

    def test_one_point(self, pt):
        """
        Ask to the bloom filter is the point is indexed
        :param pt: the point that we want to check
        :return: Boolean at true if the answer is yes, False otherwise
        """
        return pt.to_string() in self.bloom_filter

    def test_set_points(self, points):
        """
        Ask the number of element wich are in the indexed set and in the :points: set
        :param points: The set that we want to check
        :return: The size of the intersection
        """
        number_of_positif = 0
        for pt in points:
            if self.test_one_point(pt):
                number_of_positif += 1
        return number_of_positif
