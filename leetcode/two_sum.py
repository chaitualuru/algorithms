Class Solution:
	def twoSum(self, nums, target):
		self.nums_dict = {}
		for i in range(len(nums)):
			cur_num = nums[i]
			if cur_num in self.nums_dict.keys():
				return self.nums_dict[cur_num] + 1, i + 1
			else:
				self.nums_dict[target - cur_num] = i
			
					 