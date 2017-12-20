# -----------------------------------------------------------------------------------------
# Import
from src.util.Logger import Logger
from src.providerData.ReaderFromGenerator import RandomDataGenerator
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
from src.BloomFilter.BloomFilterTester import BloomFilterTester
from src.util.DataVisualisation import visualize_curve
import os
import math
import src.util.Constants as Constants
from src.providerData.ReaderFromFile import ReaderFromFile
from arf_python.ArfMain import ArfMAin
# -----------------------------------------------------------------------------------------
# Constant

# Variable : Ratio m/n
LIST_RATE=sorted(list(set(([math.floor(1.3**i) for i in range(4, 22)]))))
DIM = 2

DELTA = math.pow(2,32)/10000

# Donnes fixes
SIZE_DATA = 10000
DOMAIN = math.pow(2,32)
TESTS = 10000
REAL_SIZE = False
METHOD = [Constants.DIS_INPUTS, Constants.DIS_TESTS, Constants.DIS_DOUBLE]
ARF_METHOD = "ARF_METHOD"

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
    dic_response = create_bloom_filters(logger, METHOD)
    list_visualisation.append(dic_response[Constants.DIS_INPUTS])
    list_visualisation.append(dic_response[Constants.DIS_TESTS])
    list_visualisation.append(dic_response[Constants.DIS_DOUBLE])
    list_visualisation.append(dic_response[ARF_METHOD])
    visualize_curve(list_visualisation, "dimension", " Rate false positive (%)", "DELTA "+str(DELTA) + " N and tests "+
                    str(SIZE_DATA)+" Dim "+str(DIM)+" DOMAIN "+str(DOMAIN))




def create_bloom_filters(logger, method = None, title = "Methode : "):
    """
    Implement and create Bloom filter with different size until we reach a false positive rate minimum.
    :return: None
    """

    if method == None:
        raise Exception("Impossible de continuer sans method to discretize the space")


    # Initiate the dic response.
    dic_response = {}
    for method_cur in method:
        dic_response[method_cur] = [(title + str(method_cur)), [], []]

    dic_response[ARF_METHOD] = [(title + str(ARF_METHOD)), [], []]

    name_feed = "generate_point_feed_"
    name_test = "generate_point_test_"
    extension = "_.csv"


    list_point_feed = check_if_file_exit(DIM, "feed")
    list_point_test = check_if_file_exit(DIM, "test")

    # If the file does not exist.
    if list_point_feed == None or list_point_test == None:
        data_from_generator_feed = RandomDataGenerator(DIM, SIZE_DATA, DOMAIN)
        data_from_generator_test = RandomDataGenerator(DIM, SIZE_DATA, DOMAIN)
        data_from_generator_feed.genarate(name_feed + "DIM" + str(DIM) + "_" + "DELTA" + str(DELTA)
                                          + extension)

        # data_from_generator_test.genarate_falses_domain(delta, data_from_generator_feed.get_points())
        list_point_feed = data_from_generator_feed.get_points()

        data_from_generator_test.genarate_falses(DELTA, data_from_generator_feed.get_points(), name_test
                                                 + "DIM" + str(DIM) + "_" + "DELTA" + str(DELTA)
                                                 + extension)

        list_point_test = data_from_generator_test.get_points()

    # Loop on dim.
    for ratiomn in LIST_RATE:

        logger.info("Work for ratio : " + str(ratiomn))

        # Loop for the method used.
        for method_cur in method:

            logger.info("Work for method : " + str(method_cur))

            bloom_filter = BloomFilterTester(SIZE_DATA, SIZE_DATA * ratiomn, DIM, REAL_SIZE, list_point_feed,
                                             RectangleDiscretisator(math.floor(DELTA), method_cur))

            print("BF_OVER")
            nb_point_in_bloom_filter = bloom_filter.test_set_points(list_point_test)


            print(str(method_cur) + " "+ str(nb_point_in_bloom_filter))

            # Add result to the list.
            dic_response[method_cur][1].append(ratiomn)
            dic_response[method_cur][2].append(nb_point_in_bloom_filter / len(list_point_test))


        #-----------------------------------------
        #Arf part

        name_feed_arf = get_name_file_if_exit(DIM, "feed", extension, name_feed)
        name_test_arf = get_name_file_if_exit(DIM, "test", extension, name_test)

        if name_feed_arf == None or name_test_arf == None:
            raise Exception("Impossible to find the file")

        arf = ArfMAin(name_feed_arf, name_test_arf, DIM, DOMAIN, SIZE_DATA * ratiomn, math.floor(DELTA))
        arf.feed()
        nb_point_in_bloom_filter, nb_false_positif = arf.test()

        # Add result to the list.
        dic_response[ARF_METHOD][1].append(ratiomn)
        dic_response[ARF_METHOD][2].append(nb_false_positif / len(list_point_test))

    return dic_response

def check_if_file_exit (dim, supTest):
    dir = "../../data"
    for file in os.listdir(dir):
        dim_str = ("DIM"+ str(dim) + "_")
        delta_str = ("DELTA"+ str(DELTA)+ "_")
        if dim_str in str(file) and delta_str in str(file) and supTest in str(file):
            reader = ReaderFromFile(dim, os.path.join(dir, file))
            return reader.get_points()

    return None

def get_name_file_if_exit (dim, supTest, extension, type):
    dir = "../../data"
    for file in os.listdir(dir):
        dim_str = ("DIM"+ str(dim) + "_")
        delta_str = ("DELTA"+ str(DELTA)+ "_")
        if dim_str in str(file) and delta_str in str(file) and supTest in str(file):
            return "../../data/" + type + "DIM" +str(DIM) + "_" + "DELTA" +str(DELTA) + extension

    return None

main()