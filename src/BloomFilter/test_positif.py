from src.util.Logger import Logger
import configparser
from pathlib import Path
from src.providerData.ReaderFromFile import ReaderFromFile
from src.providerData.ReaderFromGenerator import RandomDataGenerator
from src.discretisator.RectangleDiscretisator import RectangleDiscretisator
from src.BloomFilter.BloomFilterTester import BloomFilterTester
from src.util.DataVisualisation import visualize_curve
import src.discretisator.MethodType as Method
import os


datas = RandomDataGenerator(2, 200, domain=100000, distribution=0)
datas_t = RandomDataGenerator(2, 3, domain=100000, distribution=0)
datas_tp = RandomDataGenerator(2, 100, domain=100000, distribution=0)
datas.genarate()
datas_t.genarate_falses(10, datas.get_points())
datas_tp.genarate_positives(2, datas.get_points())
print(datas.get_points())
print(datas_t.get_points())
print(datas_tp.get_points())

bloom_filter_no_dis = BloomFilterTester(200, 20000)
bloom_filter_before = BloomFilterTester(200, 20000, discretisator=RectangleDiscretisator(10, Method.DIS_TO_INSERT))
bloom_filter_double = BloomFilterTester(200, 20000, discretisator=RectangleDiscretisator(10, Method.DIS_DOUBLE))
bloom_filter_after = BloomFilterTester(200, 20000, discretisator=RectangleDiscretisator(10, Method.DIS_TO_CHECK))
print(datas.get_points())
print(datas_t.get_points())
bloom_filter_no_dis.feed(datas.get_points())
bloom_filter_before.feed(datas.get_points())
bloom_filter_double.feed(datas.get_points())
bloom_filter_after.feed(datas.get_points())
print(bloom_filter_no_dis.test_set_points(datas_t.get_points()))
print(bloom_filter_before.test_set_points(datas_t.get_points()))
print(bloom_filter_double.test_set_points(datas_t.get_points()))
print(bloom_filter_after.test_set_points(datas_t.get_points()))

print()
print()


print(bloom_filter_no_dis.test_set_points(datas_tp.get_points()))
print(bloom_filter_before.test_set_points(datas_tp.get_points()))
print(bloom_filter_double.test_set_points(datas_tp.get_points()))
print(bloom_filter_after.test_set_points(datas_tp.get_points()))

print()