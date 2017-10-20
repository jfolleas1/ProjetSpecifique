# --------------------------------------------------------------------------
# Import
import logging

# --------------------------------------------------------------------------
# Constants

# --------------------------------------------------------------------------
class Logger:
    """
    This class is the data sructure for the data that will be index by the bloom filter
    Args :
    :param dimention: int that represent dimention of the vector
    :param coordinate: list of int that are the coordinate of the vector
    """
    def __init__(self, className):
        self.logger = logging.getLogger(className)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()

        # Set the level of the logger.
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        self.logger.addHandler(ch)

    def info (self, message):
        self.logger.info(message)

    def warn (self, message):
        self.logger.warn(message)

    def debug (self, message):
        self.logger.debug(message)

    def error(self, message):
        self.logger.error(message)