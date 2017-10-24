# -----------------------------------------------------------------------------------------
# Import
from src.util.Logger import Logger
import configparser
from pathlib import Path
from src.providerData.ReaderFromFile import ReaderFromFile
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
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

    config_file = Path(PATH_CONFIG)
    print(str(config_file))
    if not config_file.is_file():
        logger.error('The config file does not exist')
        raise Exception()

    config = configparser.ConfigParser()
    config.read(PATH_CONFIG)
    reader, discritisator = getParameters (logger, config)

    # TODO call Bloom filter method.


def getParameters (logger, config):
    """
    Get parameters in config file and create the reader and the discretisator associated with the right parameters.
    :param logger: instance allowing to log
    :param config: config file
    :return: reader, discritisator with config found in config file.
    """
    try:
        reader = None
        discritisator = None

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

        if reader is None or discritisator is None:
            logger.error('The config file lacks of information to continue')
            raise Exception()

        return reader, discritisator

    except Exception as e:
        logger.error('Probleme in getting key in config file')
        raise e

main()