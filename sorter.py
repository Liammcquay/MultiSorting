import time
import sys
import Queue
import multiprocessing
from multiprocessing import Pool
from functools import partial


def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


def sortfunc(batch):
    with open(batch) as f:
        array = [int(x) for x in f]
        array = quicksort(array)
        return array


def merge(arrays):
    arr = []
    col = [0] * arrays.__len__()

    changed = True
    while changed:
        changed = False
        minVal = sys.maxint
        minRow = -1
        for i in range(0, arrays.__len__()):
            if col[i] < arrays[i].__len__() and arrays[i][col[i]] < minVal:
                minVal = arrays[i][col[i]]
                minRow = i
                changed = True

        if changed:
            arr.append(minVal)
            col[minRow] += 1

    return arr


N = 1  # Number of cores/files
print "Sorting a batch of numbers on " + str(N) + " cores : MultiCore Processing"
startTime = time.time()
batch = []  # for linear, the pool only contains 1 file


for i in range(0,N):
	batch.append("RandomNumbers" + str(i))

pool = Pool()
ret = pool.map(sortfunc, batch)

pool.close()
pool.join()

arrays = []

for a in ret:
	arrays.append(a)

sortedArray = merge(arrays)

endTime = time.time()

print "Total time taken : " + str(endTime - startTime) + "seconds"

