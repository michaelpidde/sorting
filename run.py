import copy, random, sort, time

values = range(1000)
random.shuffle(values)

def writeSortProcess(data, algorithm):
	print algorithm.__name__ + " sort...\n"
	print "Starting:\n" + str(data)
	dataCopy = copy.copy(data)
	start = time.clock()
	sorted = algorithm(dataCopy)
	end = time.clock()
	print "\nEnding:\n" + str(sorted)
	print "TIME: " + str((end - start)) + "s\n"
	print "----------------------------------------\n"

writeSortProcess(values, sort.insertion)
writeSortProcess(values, sort.selection)