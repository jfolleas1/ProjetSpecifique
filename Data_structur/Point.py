##### Aim of the file

# This file provide a class Point that will be our data strutur for the data that will fit our Bloom Filter

##### Import

import math

##### Constant


##### Code



class Point:
    """
    This class is the data sructur for the data that will be index by the bloom filter
    Args :
    :param dimention: int that represent dimention of the vector
    :param coordinate: list of int that are the coordinate of the vector
    """
    def __init__(self, dimenstion, coordinate):
        self.dimenstion = dimenstion
        self.coordinate = coordinate


    def distance(self, other_point):
        """
        Compute the distance between the current point and the other point <other_point>
        :param other_point: other point that we want to know the distant with the current point
        :return: the distance between <self> and <other_point>
        """
        sum = 0
        for tuple in zip(self.coordinate, other_point.coordinate):
            sum += tuple[0]*tuple[1]
        return math.sqrt(sum)
