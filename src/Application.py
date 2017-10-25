# -----------------------------------------------------------------------------------------
# Import
from src.util.Logger import Logger
import configparser
from pathlib import Path
from src.providerData.ReaderFromFile import ReaderFromFile
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
from src.BloomFilter.BloomFilterTester import BloomFilterTester
# -----------------------------------------------------------------------------------------
# Constant
PATH_CONFIG = './src/config.ini'

# HEADLINE-----------------------------------------
READER_FROM_FILE = 'ReaderFromFile'
GENERATE_POINT = 'GeneratePoint'
RECTANGLE_DISCRITISATOR = 'RectangleDiscritisator'
CIRCLE_DISCRITISATOR = 'CircleDiscritisator'
COMMON = 'Common'

# SUBTITLE -----------------------------------------
PATH_FILE = 'pathToFile'
DIMENSION = 'dimension'
LAMBDA_ERROR = 'lambdaError'
M = 'm'
N= 'n'
# -----------------------------------------------------------------------------------------
# Code

def main():
    """
    Run the application:
        - instanciate reader and discritisator.
        - Call method to create the Bloom filter.
        - display result.
    :return:
    """
    logger = Logger('Main')
    logger.info('begin operation on bloom filter')

    # ---------------------------------------------------------------
    # Get parameters from config file
    config_file = Path(PATH_CONFIG)
    print(str(config_file))
    if not config_file.is_file():
        logger.error('The config file does not exist')
        raise Exception()

    config = configparser.ConfigParser()
    config.read(PATH_CONFIG)
    reader, discritisator, n, m = get_parameters (logger, config)

    # Build the Bloom filter.
    bloom_filter = BloomFilterTester(n,m,reader.get_point(),discritisator)
    # TODO change read point to read point that should be tested.
    nb_point_in_bloom_filter = bloom_filter.test_set_points(reader.get_point())
    print(nb_point_in_bloom_filter)

    #TODO : visiualise result.

def get_parameters (logger, config):
    """
    Get parameters in config file and create the reader and the discretisator associated with the right parameters.
    :param logger: instance allowing to log
    :param config: config file
    :return: reader, discritisator with config found in config file.
    """
    try:
        reader = None
        discritisator = None
        m = None
        n = None

        # Select readers
        if READER_FROM_FILE in config.sections():
            reader = ReaderFromFile(config[READER_FROM_FILE][DIMENSION],
                                    config[READER_FROM_FILE][PATH_FILE])

        elif GENERATE_POINT in config.sections():
            pass

        # select discritisator
        if RECTANGLE_DISCRITISATOR in config.sections():
            discritisator = RectangleDiscretisator(config[RECTANGLE_DISCRITISATOR][LAMBDA_ERROR])

        elif CIRCLE_DISCRITISATOR in config.sections():
            pass

        if COMMON in config.sections():
            m =  RectangleDiscretisator(config[COMMON][M])
            n = RectangleDiscretisator(config[COMMON][N])

        if reader is None or discritisator is None or m is None or n is None:
            logger.error('The config file lacks of information to continue')
            raise Exception()

        return reader, discritisator, n, m

    except Exception as e:
        logger.error('Probleme in getting key in config file')
        raise e

main()