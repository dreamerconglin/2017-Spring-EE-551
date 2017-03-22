import math
import time

print (math.pi)
print (math.sqrt(45))

start = time.clock()
for x in range(100000):
    pass
stop = time.clock()

print ("It took this long: ", stop - start)
