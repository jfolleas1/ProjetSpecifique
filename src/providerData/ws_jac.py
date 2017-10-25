from src.providerData.ReaderFromGenerator import RandomDataGenerator
print("DIM 1")
feed_dim1 = RandomDataGenerator(1, size_of_data_set=200, domain=10000)
feed_dim1.genarate("feed_dim1")

test_dim1_delta_2 = RandomDataGenerator(1, size_of_data_set=200, domain=10000)
test_dim1_delta_2.genarate_falses(2, feed_dim1.get_points(), save_file_name="test_dim1_delta_2")
print("passsed")

test_dim1_delta_5 = RandomDataGenerator(1, size_of_data_set=200, domain=10000)
test_dim1_delta_5.genarate_falses(5, feed_dim1.get_points(), save_file_name="test_dim1_delta_5")
print("passsed")

test_dim1_delta_10 = RandomDataGenerator(1, size_of_data_set=200, domain=10000)
test_dim1_delta_10.genarate_falses(10, feed_dim1.get_points(), save_file_name="test_dim1_delta_10")
print("passed")

print("DIM 2")

feed_dim2 = RandomDataGenerator(2, size_of_data_set=200, domain=10000)
feed_dim2.genarate("feed_dim2")

test_dim2_delta_2 = RandomDataGenerator(2, size_of_data_set=200, domain=10000)
test_dim2_delta_2.genarate_falses(2, feed_dim2.get_points(), save_file_name="test_dim2_delta_2")
print("passsed")

test_dim2_delta_5 = RandomDataGenerator(2, size_of_data_set=200, domain=10000)
test_dim2_delta_5.genarate_falses(5, feed_dim2.get_points(), save_file_name="test_dim2_delta_5")
print("passsed")

test_dim2_delta_10 = RandomDataGenerator(2, size_of_data_set=200, domain=10000)
test_dim2_delta_10.genarate_falses(10, feed_dim2.get_points(), save_file_name="test_dim2_delta_10")
print("passed")

print("DIM 3")

feed_dim3 = RandomDataGenerator(3, size_of_data_set=200, domain=10000)
feed_dim3.genarate("feed_dim3")

test_dim3_delta_2 = RandomDataGenerator(3, size_of_data_set=200, domain=10000)
test_dim3_delta_2.genarate_falses(2, feed_dim3.get_points(), save_file_name="test_dim3_delta_2")
print("passsed")

test_dim3_delta_5 = RandomDataGenerator(3, size_of_data_set=200, domain=10000)
test_dim3_delta_5.genarate_falses(5, feed_dim3.get_points(), save_file_name="test_dim3_delta_5")
print("passsed")

test_dim3_delta_10 = RandomDataGenerator(3, size_of_data_set=200, domain=10000)
test_dim3_delta_10.genarate_falses(10, feed_dim3.get_points(), save_file_name="test_dim3_delta_10")
print("passed")