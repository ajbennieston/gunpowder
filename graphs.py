import math
import operator

from ROOT import TGraph, TGraphErrors

from dynamic_binning import Binner
from statistics import mean, standard_deviation

__all__ = ['graph', 'graph_errors', 'binned_means_graph_errors']

def graph(data, name, title='', xlabel='', ylabel=''):
	# Expect data to be of the form
	# [(x,y), ...]
	N = len(data)
	g = TGraph(N)
	g.SetName(name)
	title = "%s;%s;%s" % (title, xlabel, ylabel)
	g.SetTitle(title)
	cur_pt = 0
	for d in data:
		g.SetPoint(cur_pt, d[0], d[1])
		cur_pt += 1
	return g

def graph_errors(data, name, title='', xlabel='', ylabel=''):
	# Expect data to be of the form:
	# [(x, y, dx, dy), ...]
	N = len(data)
	g = TGraphErrors(N)
	g.SetName(name)
	title = "%s;%s;%s" % (name, xlabel, ylabel)
	g.SetTitle(title)
	cur_pt = 0
	for d in data:
		g.SetPoint(cur_pt, d[0], d[1])
		g.SetPointError(cur_pt, d[2], d[3])
		cur_pt += 1
	return g

def binned_means_graph_errors(data, name, min_count=10, min_width=10, title='', xlabel='', ylabel=''):
	# Expect data to be of the form:
	# [(x,y), ...]
	data = sorted(data, key=operator.itemgetter(0))
	binner = Binner(data, min_count, min_width)
	binner.bin()
	pieces = binner.get_bins()
	points = [ ]
	for piece in pieces:
		xdata, ydata = zip(*piece)
		# x error is bin width / 2
		xmax = max(xdata)
		xmin = min(xdata)
		xwidth = xmax - xmin
		xcentre = xmin + (xwidth / 2.0)
		xerror = xwidth / 2
		ymean = mean(ydata)
		ysigma = standard_deviation(ydata, ymean)
		yerror = ysigma / math.sqrt(len(ydata))
		points.append((xcentre, ymean, xerror, yerror))
	return graph_errors(points, name, title=title, xlabel=xlabel, ylabel=ylabel)



