import unittest
from src.providerData.ReaderFromFile import ReaderFromFile
from src.structureData.Point import Point

REPOSITORY_PATH = "./tests/data/"
FILE_NAME = "test.txt"
FILE_NAME_FAIL = "test_fail.txt"
DIMENSION = 2
LENGHT_POINTS = 3

class PointTest(unittest.TestCase):
    """Test case used for test my ReadearFile class."""

    def setUp(self):
        """Initialize tests."""
        self.reader_file1 = ReaderFromFile(DIMENSION, REPOSITORY_PATH, FILE_NAME)
        self.reader_file2 = ReaderFromFile(DIMENSION, REPOSITORY_PATH, FILE_NAME_FAIL)

    def test_reader(self):
        """Test of function get Point."""
        list_point = self.reader_file1.get_points()
        self.assertEqual(len(list_point),LENGHT_POINTS, "The lenght of the list are not equal")
        for point in list_point:
            assert (type(point) == Point)

    def test_exeption(self):
        """Test of raising exception. """
        self.assertRaises(Exception,self.reader_file2.get_points)

unittest.main()