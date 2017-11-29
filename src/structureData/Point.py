# -----------------------------------------------------------------------------------------
# Aim of the file

# This file provide a class Point that will be our data strutur for the data that will fit our Bloom Filter

# -----------------------------------------------------------------------------------------
# Import

import math

# -----------------------------------------------------------------------------------------
# Constant

CONST_APPROXIMATION = 1000000

# -----------------------------------------------------------------------------------------
# Code


class Point:
    """
    This class is the data sructure for the data that will be index by the bloom filter
    Args :
    :param dimention: int that represent dimention of the vector
    :param coordinate: list of int that are the coordinate of the vector
    """
    def __init__(self, coordinates):
        assert (type(coordinates) == list)
        self.coordinates = list(map((lambda x: float(x)), coordinates))
        self.dimension = len(coordinates)

    def __eq__(self, other):
        return self.distance(other) == 0

    def __repr__(self):

        return "Pt d"+str(self.dimension)+" : "+self.coordinates.__repr__()

    def to_string(self):
        res = ""
        for i in self.coordinates:
            res += ":"+str(math.floor(i*CONST_APPROXIMATION)/CONST_APPROXIMATION)
        return res[1:]

    def distance(self, other_point):
        """
        Compute the distance between the current point and the other point <other_point>
        :param other_point: other point that we want to know the distant with the current point
        :return: the distance between <self> and <other_point>
        """
        sum = 0
        for tuple in zip(self.coordinates, other_point.coordinates):
            sum += (tuple[0]-tuple[1])**2
        return math.sqrt(sum)


