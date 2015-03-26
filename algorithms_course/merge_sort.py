def merge_sort(nums):
	if len(nums) == 1:
		return nums
	# final sorted list
	sort = []
	# length of array
	nums_len = len(nums)
	# first array's end index
	first = nums_len // 2
	sorted_first = merge_sort(nums[:first])
	first_len = len(sorted_first)
	sorted_second = merge_sort(nums[first:nums_len])
	second_len = len(sorted_second)
	first_index = 0
	second_index = 0
	for i in range(nums_len):
		if first_index != first_len and second_index != second_len:
			if sorted_first[first_index] > sorted_second[second_index]:
				sort.append(sorted_second[second_index])
				second_index += 1
			else:
				sort.append(sorted_first[first_index])
				first_index += 1
		else:
			if first_index > second_index:
				sort.extend(sorted_second[second_index:])
			else:
				sort.extend(sorted_first[first_index:])
			break
	return sort

print merge_sort([5,4,2,3,1,7,8,9,10,11])
