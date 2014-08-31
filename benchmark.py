import copy, random, sort, time


algorithms = [sort.insertion, sort.selection]


def runGroup(count, algorithms):
	values = range(count)
	results = []
	for algorithm in algorithms:
		data = copy.copy(values)
		start = time.clock()
		result = algorithm(data)
		runTime = time.clock() - start
		results.append({
			"algorithm": algorithm.__name__,
			"time": runTime,
			"count": count
		})
	return results


def iterate(count):
	results = []
	for i in range(count):
		results.append(runGroup(10000, algorithms))
	return results


def benchmark():
	iterations = 10
	results = iterate(iterations)
	totals = [[] for i in range(len(algorithms))]

	for group in results:
		for item in group:
			for index, algorithm in enumerate(algorithms):
				if item.get('algorithm') == algorithm.__name__:
					totals[index].append(item.get('time'))

	print "-- Averages over " + str(iterations) + " iterations --\n"
	for index, group in enumerate(totals):
		print algorithms[index].__name__ + " sort: {0:.2f} seconds\n".format((sum(group) / iterations))