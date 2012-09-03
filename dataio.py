#!/usr/bin/env python

def _determine_conversion(flag):
    if flag == 'I':
        return lambda x : int(x)
    elif flag == 'F':
        return lambda x : float(x)
    else:
        return lambda x : None # still callable!

def _get_stripped_lines(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def _split(lines, delimiter):
    return [l.split(delimiter) for l in lines]

# Generic data input function
def read_data(filename, typelist, delimiter=' '):
    converters = [_determine_conversion(t) for t in typelist]
    return [map(lambda f, x: f(x),
        converters,
        d) for d in _split(_get_stripped_lines(filename), delimiter)]

# Convenience functions based on the definition above
def read_x(filename, type1='I', delimiter=' '):
    # for 1D data, flatten the list
    return [item for sublist in read_data(filename, [type1], delimiter) for item in sublist]

def read_xy(filename, type1='I', type2='I', delimiter=' '):
    return read_data(filename, [type1, type2], delimiter)

def read_xyz(filename, type1='I', type2='I', type3='I', delimiter=' '):
    return read_data(filename, [type1, type2, type3], delimiter)

