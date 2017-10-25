# -----------------------------------------------------------------------------------------
# Import
from src.util.Logger import Logger
import configparser
from pathlib import Path
from src.providerData.ReaderFromFile import ReaderFromFile
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
from src.BloomFilter.BloomFilterTester import BloomFilterTester
from src.util.DataVisualisation import visualize_curve
import os
# -----------------------------------------------------------------------------------------
# Constant
PATH_CONFIG = './config/'

# HEADLINE-----------------------------------------
READER_FROM_FILE = 'ReaderFromFile'
GENERATE_POINT = 'GeneratePoint'
RECTANGLE_DISCRITISATOR = 'RectangleDiscritisator'
CIRCLE_DISCRITISATOR = 'CircleDiscritisator'
COMMON = 'Common'


# SUBTITLE -----------------------------------------
PATH_FILE_FEED = 'pathToFileFeed'
DIMENSION = 'dimension'
LAMBDA_ERROR = 'lambdaError'
PATH_FILE_TEST = 'pathToFileTest'
M = 'm'
# -----------------------------------------------------------------------------------------
# Code

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
    for fn in os.listdir(PATH_CONFIG):
        list_visualisation.append(run_test_on_bloom_filter(logger, PATH_CONFIG, fn))

    visualize_curve(list_visualisation,"test_x", "test_y","title")


def run_test_on_bloom_filter(logger, Path_config, file_name):
    """
    Run the application:
        - instanciate reader and discritisator.
        - Call method to create the Bloom filter.
        - display result.
    :return:
    """
    config_file = Path(Path_config + file_name)
    if not config_file.is_file():
        logger.error('The config file does not exist')
        raise Exception()

    logger.info('Read config information on : ' + str(Path_config + file_name))
    config = configparser.ConfigParser()
    config.read(Path_config + file_name)
    list_point_feed, list_point_test, discritisator, m = get_parameters(logger, config)

    # Build the Bloom filter.
    bloom_filter = BloomFilterTester(len(list_point_feed), m, list_point_feed, discritisator)
    nb_point_in_bloom_filter = bloom_filter.test_set_points(list_point_test)

    return ("Test", [m/len(list_point_feed)], [nb_point_in_bloom_filter])

def get_parameters (logger, config):
    """
    Get parameters in config file and create the reader and the discretisator associated with the right parameters.
    :param logger: instance allowing to log
    :param config: config file
    :return: reader, discritisator with config found in config file.
    """
    try:
        discritisator = None
        m = None
        list_point_feed = None
        list_point_test = None

        # Select readers
        if READER_FROM_FILE in config.sections():
            reader_feed = ReaderFromFile(int(config[READER_FROM_FILE][DIMENSION]),
                                    config[READER_FROM_FILE][PATH_FILE_FEED])
            list_point_feed = reader_feed.get_points()

            reader_test = ReaderFromFile(int(config[READER_FROM_FILE][DIMENSION]),
                                    config[READER_FROM_FILE][PATH_FILE_TEST])
            list_point_test = reader_test.get_points()

        elif GENERATE_POINT in config.sections():
            #TODO
            pass

        # select discritisator
        if RECTANGLE_DISCRITISATOR in config.sections():
            discritisator = RectangleDiscretisator(config[RECTANGLE_DISCRITISATOR][LAMBDA_ERROR])

        elif CIRCLE_DISCRITISATOR in config.sections():
            #TODO
            pass


        if COMMON in config.sections():
            m = config[COMMON][M]

        if list_point_feed is None or \
                        list_point_test is None or \
                        discritisator is None or \
                        m is None:
            logger.error('The config file lacks of information to continue')
            raise Exception()

        return list_point_feed, list_point_test, discritisator, int(m)

    except Exception as e:
        logger.error('Probleme in getting key in config file')
        raise e

main()