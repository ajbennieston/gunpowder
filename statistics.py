__all__ = ['mean', 'standard_deviation']

import math

def mean(data):
	N = float(len(data))
	return sum(data) / N

def standard_deviation(data, mu):
	N = float(len(data))
	return math.sqrt(sum((x-mu)**2 for x in data) / N)


