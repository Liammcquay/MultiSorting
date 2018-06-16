import time
import sys
import Queue
from thread import start_new_thread, allocate_lock

N = 1  # Number of threads/files
num_threads = 0
thread_started = False
lock = allocate_lock()


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
        # Don't forget to return something!
        return quicksort(less) + equal + quicksort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


def sortfunc(batch, q):
    global num_threads, thread_started
    lock.acquire()
    num_threads += 1
    thread_started = True
    lock.release()
    with open(batch) as f:
        array = [int(x) for x in f]
        array = quicksort(array)
        q.put(array)
    lock.acquire()
    num_threads -= 1
    lock.release()
    

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


print("Sorting on " + str(N) + " threads")
startTime = time.time()

q = Queue.Queue()

for i in range(0, N):
    start_new_thread(sortfunc, ("RandomNumbers" + str(i),q))

while not thread_started:
    pass
while num_threads > 0:
    pass

arrays = []

for i in range(0, q.qsize()):
	arrays.append(q.get())

sortedArray = merge(arrays)

endTime = time.time()

print "Total time taken : " + str(endTime - startTime) + "seconds"








