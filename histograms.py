#!/usr/bin/env python
import math

from ROOT import TH2I, TH2F, TH2D, TH1I, TH1F, TH1D

__all__ = ['histogram_2D', 'histogram_1D']

def histogram_2D(data, xwidth, ywidth, name, title='', xlabel='', ylabel='', xmin=None, xmax=None, ymin=None, ymax=None, type='I'):
	# Expect data to be of the form [(x, y, weight), ...]
	x_, y_, weight_ = zip(*data)
	if xmin is None:
		xmin = min(x_)
	if xmax is None:
		xmax = max(x_)
	if ymin is None:
		ymin = min(y_)
	if ymax is None:
		ymax = max(y_)

	# Adjust minima to a bin boundary
	xmin = (xmin + xwidth) - ((xmin + xwidth) % xwidth) - xwidth
	ymin = (ymin + ywidth) - ((ymin + ywidth) % ywidth) - ywidth

	# Adjust maxima to a bin boundary
	xmax = (xmax + xwidth) - ((xmax + xwidth) % xwidth)
	ymax = (ymax + ywidth) - ((ymax + ywidth) % ywidth)

	nbins_x = int(math.ceil((xmax - xmin) / xwidth))
	nbins_y = int(math.ceil((ymax - ymin) / ywidth))

	# Create histogram
	hist_title = "%s;%s;%s" % (title, xlabel, ylabel)
	hist = None
	if type == 'I':
		hist = TH2I(name, hist_title, nbins_x, xmin, xmax, nbins_y, ymin, ymax)
	elif type == 'F':
		hist = TH2F(name, hist_title, nbins_x, xmin, xmax, nbins_y, ymin, ymax)
	else:
		hist = TH2D(name, hist_title, nbins_x, xmin, xmax, nbins_y, ymin, ymax)
	
	for entry in data:
		hist.Fill(entry[0], entry[1], entry[2])
	
	# Return the histogram
	return hist

def simple_histogram_1D(data, xwidth, name, title='', xlabel='', ylabel='', xmin=None, xmax=None, type='I'):
    # Takes a simple list of numbers
    # Just set all weights to 1 and pass data to the histogram_1D variant
    weighted_data = [(d,1) for d in data]
    return histogram_1D(weighted_data, xwidth, name, title, xlabel, ylabel, xmin, xmax, type)

def histogram_1D(data, xwidth, name, title='', xlabel='', ylabel='', xmin=None, xmax=None, type='I'):
	# Expect data to be of the form [(x, weight), ...]
	x_, weight_ = zip(*data)
	xmin = min(x_)
	xmax = max(x_)

	# Adjust min / max to bin boundaries
	xmin = (xmin + xwidth) - ((xmin + xwidth) % xwidth) - xwidth
	xmax = (xmax + xwidth) - ((xmax + xwidth) % xwidth)

	nbins_x = int(math.ceil((xmax - xmin) / xwidth))

	# Create histogram
	hist_title = "%s;%s;%s" % (title, xlabel, ylabel)
	hist = None
	if type == 'I':
		hist = TH1I(name, title, nbins_x, xmin, xmax)
	elif type == 'F':
		hist = TH1F(name, title, nbins_x, xmin, xmax)
	else:
		hist = TH1D(name, title, nbins_x, xmin, xmax)

	for entry in data:
		hist.Fill(entry[0], entry[1])
	
	return hist

def histogram_1D_errors(data, xwidth, name, title='', xlabel='', ylabel='', xmin=None, xmax=None, type='I'):
	# Expect data of the form [(x, weight, error), ...]
	x_, weight_, err_ = zip(*data)
	xmin = min(x_)
	xmax = max(x_)

	# Adjust min / max to bin boundaries
	xmin = (xmin + xwidth) - ((xmin + xwidth) % xwidth) - xwidth
	xmax = (xmax + xwidth) - ((xmax + xwidth) % xwidth)

	nbins_x = int(math.ceil((xmax - xmin) / xwidth))

	# Create histogram
	hist_title = "%s;%s;%s" % (title, xlabel, ylabel)
	hist = None
	if type == 'I':
		hist = TH1I(name, title, nbins_x, xmin, xmax)
	elif type == 'F':
		hist = TH1F(name, title, nbins_x, xmin, xmax)
	else:
		hist = TH1D(name, title, nbins_x, xmin, xmax)

	for entry in data:
		bin = hist.GetXaxis().FindBin(entry[0])
		hist.SetBinContent(bin, entry[1])
		hist.SetBinError(bin, entry[2])
	
	return hist

