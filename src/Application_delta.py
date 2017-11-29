# -----------------------------------------------------------------------------------------
# Import
from src.util.Logger import Logger
import configparser
from pathlib import Path
from src.providerData.ReaderFromFile import ReaderFromFile
from src.providerData.ReaderFromGenerator import RandomDataGenerator
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
from src.discretisator.CircleDiscretisor2D import CircleDiscretisator2D
from src.BloomFilter.BloomFilterTester import BloomFilterTester
from src.util.DataVisualisation import visualize_curve
import src.util.Constants as Constants
from src.discretisator.Arf import Arf
import math
import os
# -----------------------------------------------------------------------------------------
# Constant



DIMENSION = 2
SIZE_DATA = 250
DOMAIN = 5000
RATE_M_N = 100
TESTS = 250
REAL_SIZE = True



def main():
    """
        loop throught all config file and display result.
    :return:
    """
    logger = Logger('Main')
    logger.info('begin operation on bloom filter')




    # ---------------------------------------------------------------
    # Get parameters from config file
    list_visualisation = [];
    a = create_bloom_filters(logger)
    list_visualisation.append(("dis_input", a[0], a[1][0]))
    list_visualisation.append(("dis_test", a[0], a[1][1]))
    list_visualisation.append(("dis_double", a[0], a[1][2]))
    list_visualisation.append(("dis_circle", a[0], a[1][3]))
    list_visualisation.append(("arf", a[0], a[1][4]))
    #list_visualisation.append(("dis_none", a[0], a[1][3]))
    visualize_curve(list_visualisation, "delta", " rate false positive (%)", "Dimension: "+str(DIMENSION) + "   size_set n: "+str(SIZE_DATA)+"   rate size_bloom/size_set n/m: "+str(RATE_M_N)+"    domain: "+str(DOMAIN)+ "   number_of tests: "+ str(TESTS))




def create_bloom_filters(logger):
    """
    Implement and create Bloom filter with different size until we reach a false positive rate minimum.
    :return: None
    """

    list_delta = []
    false_positive_rate = [[], [], [], [], []]
    k = 0;
    name_feed = "generate_point_feed.csv"
    name_test = "generate_point_test.csv"
    arf = Arf('./arf')

    for delta in range(1, 50, 2):

        data_from_generator_feed = RandomDataGenerator(DIMENSION, SIZE_DATA, DOMAIN)
        data_from_generator_test = RandomDataGenerator(DIMENSION, SIZE_DATA, DOMAIN)
        data_from_generator_feed.genarate(name_feed)


        list_point_feed = data_from_generator_feed.get_points()
        list_point_test = data_from_generator_test.get_points()
        data_from_generator_test.genarate_falses(delta, data_from_generator_feed.get_points(),name_test)
        discretizator = None


        bloom_filter_RI = BloomFilterTester(SIZE_DATA, SIZE_DATA * RATE_M_N, DIMENSION, REAL_SIZE, list_point_feed, RectangleDiscretisator(delta, Constants.DIS_INPUTS))
        bloom_filter_RT = BloomFilterTester(SIZE_DATA, SIZE_DATA * RATE_M_N, DIMENSION, REAL_SIZE, list_point_feed, RectangleDiscretisator(delta, Constants.DIS_TESTS))
        bloom_filter_D = BloomFilterTester(SIZE_DATA, SIZE_DATA * RATE_M_N, DIMENSION, REAL_SIZE, list_point_feed, RectangleDiscretisator(delta, Constants.DIS_DOUBLE))
        bloom_filter_C = BloomFilterTester(SIZE_DATA, SIZE_DATA * RATE_M_N, DIMENSION, REAL_SIZE, list_point_feed, CircleDiscretisator2D(delta, Constants.DIS_INPUTS))
        false_positive_rate[0].append(bloom_filter_RI.test_set_points(list_point_test)/ SIZE_DATA)
        false_positive_rate[1].append(bloom_filter_RT.test_set_points(list_point_test)/ SIZE_DATA)
        false_positive_rate[2].append(bloom_filter_D.test_set_points(list_point_test) / SIZE_DATA)
        false_positive_rate[3].append(bloom_filter_C.test_set_points(list_point_test) / SIZE_DATA)

        # ---------------------------------------------------------------------------      ARF part.
        argv =  [str(math.log(DOMAIN/delta, 2)), str(delta), str(DIMENSION), str(SIZE_DATA), str(SIZE_DATA * RATE_M_N),
                    "../data/"+name_feed, "../data/"+name_test]
        size_filter_real, false_positive = arf.execute_program(argv);
        false_positive_rate[4].append(int(false_positive) / SIZE_DATA)
        # -------------------------------------------------------------------------

        # Add result to the list.
        list_delta.append(delta)

    return [list_delta, false_positive_rate]

main()