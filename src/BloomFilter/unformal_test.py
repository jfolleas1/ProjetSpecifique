from src.providerData.ReaderFromGenerator import RandomDataGenerator
from src.BloomFilter.BloomFilterTester import BloomFilterTester
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator


print("DIM 1")
feed_dim1 = RandomDataGenerator(3, size_of_data_set=500, domain=100000)
feed_dim1.genarate()

test_dim1_delta_2 = RandomDataGenerator(3, size_of_data_set=500, domain=100000)
test_dim1_delta_2.genarate_falses(5, feed_dim1.get_points(), save_file_name="toto")

bf = BloomFilterTester(500,8000)
discretizor = RectangleDiscretisator(5)
bf.feed(feed_dim1.get_points(), discretizor)
print("BF SIZE : " + str(bf._get_bf_size()))
print(test_dim1_delta_2.point_list.__len__())
print(bf.test_set_points(test_dim1_delta_2.get_points(), discretizor))