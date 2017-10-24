import unittest
from src.BloomFilter.BloomFilterTester import BloomFilterTester


class PointTest(unittest.TestCase):
    """Test case used for test my Point class."""

    def setUp(self):
        """Initialize tests."""
        self.bf_tester = BloomFilterTester(10, 80)

    def test_bf_size(self):
        """Test of function distance."""
        self.assertEqual(80, self.bf_tester._get_bf_size())

