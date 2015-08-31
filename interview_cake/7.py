class TempTracker(object):

	def __init__(self):
		self.max_temp = None
		self.min_temp = None
		self.mean = None
		self.mode = None
		self.total = 0
		self.num = 0
		self.temps = [0] * 111
		self.max_occurs = 0

	def __insert__(self, temp):
		self.temps[temp] += 1
		if self.temps[temp] > max_occurs:
			self.mode = temp
			self.max_occurs = self.temps[temps]

		self.total += temp
		self.num += 1
		self.mean = self.total/self.num

		if temp > self.max_temp or not self.max_temp:
			self.max_temp = temp

		if temp < self.min_temp or not self.min_temp:
			self.min_temp = tem

	def get_min(self):
		return self.min_temp

	def get_max(self):
		return self.max_temp

	def get_mean(self):
		return self.mean

	def get_mode(self):
		return self.mode

