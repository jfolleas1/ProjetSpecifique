from src.providerData.ReaderFromGenerator import RandomDataGenerator

feed_dim1 = RandomDataGenerator(1, size_of_data_set=200, domain=10000)
feed_dim1.genarate("feed_dim1")

test_dim1_delta_5 = RandomDataGenerator(1, size_of_data_set=200, domain=10000)
test_dim1_delta_5.genarate_falses(2, feed_dim1.get_points(), save_file_name="test_dim1_delta_5")
print("passsed")

test_dim1_delta_10 = RandomDataGenerator(1, size_of_data_set=200, domain=10000)
test_dim1_delta_10.genarate_falses(5, feed_dim1.get_points(), save_file_name="test_dim1_delta_10")
print("passsed")

test_dim1_delta_20 = RandomDataGenerator(1, size_of_data_set=200, domain=10000)
test_dim1_delta_20.genarate_falses(10, feed_dim1.get_points(), save_file_name="test_dim1_delta_20")