
class Binner(object):
	def __init__(self, data, min_count, min_width):
		self.data = data
		self.min_count = min_count
		self.min_width = min_width
		self.current_point = 0
		self.bins = [ ]

	def get_bins(self):
		return self.bins

	def _get_next_points(self, n):
		i = self.current_point
		self.current_point += n
		return self.data[i:i+n]

	def bin(self):
		done = False
		while not done:
			bin, done = self._fill_a_bin()
			if len(bin):
				self.bins.append(bin)

	def _fill_a_bin(self):
		# First, ensure there are at least min_count points
		bin = self._get_next_points(self.min_count)
		if len(bin) < self.min_count:
			# we've run out of data; this will have to do
			return (bin, True)
		# Otherwise test if bin is wide enough
		top = max(x[0] for x in bin)
		btm = min(x[0] for x in bin)
		while top - btm < self.min_width:
			more = list(self._get_next_points(1))
			if not len(more):
				# Ran out of data
				return (bin, True)
			bin.extend(more)
			top = max(x[0] for x in bin)
			btm = min(x[0] for x in bin)
		# Now we have a bin that is wide enough *and*
		# contains enough points, or we've run out of points
		return (bin, False)

