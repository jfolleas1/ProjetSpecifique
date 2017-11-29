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
import src.util.Constants as Method
import os
# -----------------------------------------------------------------------------------------
# Constant



DELTA = 10
SIZE_DATA = 500
DOMAIN = 500
RATE_M_N = 100
TESTS = 150
REAL_SIZE = False



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
    list_visualisation.append(create_bloom_filters(logger,  Method.DIS_INPUTS))
    list_visualisation.append(create_bloom_filters(logger, Method.DIS_TESTS))
    list_visualisation.append(create_bloom_filters(logger, Method.DIS_DOUBLE))
    visualize_curve(list_visualisation, "dimension", " rate false positive (%)", "DELTA "+str(DELTA) + " N "+str(SIZE_DATA)+" M/N "+str(RATE_M_N)+" DOMAIN "+str(DOMAIN)+ " Tests "+ str(TESTS))




def create_bloom_filters(logger, method = None, title = "Methode : "):
    """
    Implement and create Bloom filter with different size until we reach a false positive rate minimum.
    :return: None
    """

    list_dim = []
    false_positive_rate = []
    k = 0;
    for dim in range(3, 8):

        data_from_generator_feed = RandomDataGenerator(dim, SIZE_DATA, DOMAIN)
        data_from_generator_test = RandomDataGenerator(dim, SIZE_DATA, DOMAIN)
        data_from_generator_feed.genarate()

        # data_from_generator_test.genarate_falses_domain(delta, data_from_generator_feed.get_points())
        list_point_feed = data_from_generator_feed.get_points()
        list_point_test = data_from_generator_test.get_points()
        data_from_generator_test.genarate_falses(DELTA, data_from_generator_feed.get_points())
        discretizator = None
        if method:
            discretizator = RectangleDiscretisator(DELTA, method)
            bloom_filter = BloomFilterTester(SIZE_DATA, SIZE_DATA*RATE_M_N, dim, REAL_SIZE, list_point_feed, RectangleDiscretisator(DELTA, method))
        nb_point_in_bloom_filter = bloom_filter.test_set_points(list_point_test)
        # Add result to the list.
        list_dim.append(dim)
        false_positive_rate.append(nb_point_in_bloom_filter/ len(list_point_test))

    return (title + str(method)), list_dim, false_positive_rate



main()