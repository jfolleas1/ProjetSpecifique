# -----------------------------------------------------------------------------------------
# Import
from src.util.Logger import Logger
import configparser
from pathlib import Path
from src.providerData.ReaderFromFile import ReaderFromFile
from src.providerData.ReaderFromGenerator import RandomDataGenerator
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
from src.BloomFilter.BloomFilterTester import BloomFilterTester
from src.util.DataVisualisation import visualize_curve
import src.discretisator.MethodType as Method
import os
# -----------------------------------------------------------------------------------------
# Constant



DIMENSION = 2
SIZE_DATA = 30
DOMAIN = 100
RATE_M_N = 100
TESTS = 300



def main():
    """
        loop throught all config file and display result.
    :return:
    """
    logger = Logger('Main')
    logger.info('begin operation on bloom filter')

    # ---------------------------------------------------------------
    # Get parameters from config file
    list_visualisation = []
    list_visualisation.append(create_bloom_filters(logger, "dis_double"))
    list_visualisation.append(create_bloom_filters(logger, "dis_to_insert"))
    list_visualisation.append(create_bloom_filters(logger, "dis_to_check"))
    list_visualisation.append(create_bloom_filters(logger))
    visualize_curve(list_visualisation, "delta", " rate false positive (%)", "DIM "+str(DIMENSION) + " N "+str(SIZE_DATA)+" M/N "+str(RATE_M_N)+" DOMAIN "+str(DOMAIN)+ " Tests "+ str(TESTS))




def create_bloom_filters(logger, method = None, title = "Methode : "):
    """
    Implement and create Bloom filter with different size until we reach a false positive rate minimum.
    :return: None
    """

    list_delta = []
    false_positive_rate = []
    for delta in range(1, 20, 2):
        data_from_generator_feed = RandomDataGenerator(DIMENSION, SIZE_DATA, DOMAIN)
        data_from_generator_feed.genarate()
        data_from_generator_test = RandomDataGenerator(DIMENSION, TESTS, DOMAIN)
        #data_from_generator_test.genarate_falses(delta, data_from_generator_feed.get_points())
        data_from_generator_test.genarate_falses_domain(delta, data_from_generator_feed.get_points())
        list_point_feed = data_from_generator_feed.get_points()
        list_point_test = data_from_generator_test.get_points()
        discretizator = None
        if method:
            discretizator = RectangleDiscretisator(delta, method)
        bloom_filter = BloomFilterTester(len(list_point_feed)*2**DIMENSION, SIZE_DATA*RATE_M_N*2**DIMENSION, list_point_feed, discretizator)
        nb_point_in_bloom_filter = bloom_filter.test_set_points(list_point_test)
        # Add result to the list.
        list_delta.append(delta)
        false_positive_rate.append(nb_point_in_bloom_filter/ len(list_point_test))
        diffFalsePositive = nb_point_in_bloom_filter

    return (title + str(method)), list_delta, false_positive_rate



main()