import unittest

from src.providerData.ReaderFromGenerator import RandomDataGenerator
from src.BloomFilter.BloomFilterTester import BloomFilterTester
from src.structureData.Point import Point
from src.discretisator.CircleDiscretisor2D import CircleDiscretisator2D


class PointTest(unittest.TestCase):
    """Test case used for test my Point class."""

    def setUp(self):
        """Initialize tests."""
        self.bf_tester = BloomFilterTester(10, 8000, 2, discretisator=CircleDiscretisator2D(5))
        self.bf_tester.feed([Point([5, 5])])
        self.discretized_points = [Point([5, 5]), Point([5,6]), Point([5, 4]), Point([6, 5]), Point([4, 5]),
                                   Point([4, 7]), Point([101,90])]

        # Second test


        dim = 2
        delta = 5
        feed_data = RandomDataGenerator(dim, size_of_data_set=200, domain=1000000)
        feed_data.genarate()

        self.similar_data = RandomDataGenerator(dim, size_of_data_set=200, domain=1000000)
        self.similar_data.genarate_similar(delta, feed_data.get_points())

        Cdiscretizor = CircleDiscretisator2D(10)

        self.bf2 = BloomFilterTester(200, 3200, 2, discretisator=Cdiscretizor)
        self.bf2.feed(feed_data.get_points())

    def test_test_set_points(self):
        """Test if the check a all set of point work"""
        self.assertEqual(6,self.bf_tester.test_set_points(self.discretized_points), "error in test_test_set_points")

    def test_no_false_negative(self):
        """Test if the discretization did not produce any false negative"""
        false_negative_rate = (200 - self.bf2.test_set_points(self.similar_data.get_points())) / 2.0
        self.assertEqual(0.0,false_negative_rate, "The bloom filter generate flase negative")
