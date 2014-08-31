import argparse, benchmark, copy, random, sort, time

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--benchmark", action='store_true', help="Run benchmarking")
args = parser.parse_args()

if args.benchmark:
	benchmark.benchmark()
else:
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