import random, time, sort

values = range(100)
random.shuffle(values)

print "Starting:\n" + str(values)

start = time.clock()
sorted = sort.insertion(values)
end = time.clock()
print "Ending:\n" + str(sorted)
print "Time: " + str((end - start) * 60) + "s"