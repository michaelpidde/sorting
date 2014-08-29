def insertion(values):
	sorted = []
	while len(values):
		value = values.pop()
		if len(sorted) == 0 or sorted[len(sorted) - 1] <= value:
			# If the sorted array has no items yet or the current value is larger than all others
			# (the largest value will always be the highest index)
			# just append the value to the end of the sorted array
			sorted.append(value)
			continue
		else:
			# inject into sorted accordingly
			for index, compare in enumerate(sorted):
				if compare >= value:
					# If the value is less or equal to what we're comparing to, 
					# insert the value where we're at in the sorted array.
					sorted.insert(index, value)
					break
				if index == len(sorted) - 1:
					# If we're at this point then we've gone through the full array and the current value is the lowest of the bunch. 
					# Insert it at the head.
					sorted.insert(0, value)
	return sorted