import random  # importing a library which gives additional functionality
import time
import sys
import queue
import multiprocessing
from multiprocessing import Pool
from functools import partial

import os

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

def rand(start, end, num):  # Populates the array with random numbers in the given range
    res = []

    for j in range(num):
        res.append(random.randint(start, end))
    print(str(num) + " ints generated")
    return res


def partition(arr, n):
    length = arr.__len__()
    frac = float(length) / n
    sen = 0.0
    parts = []

    for i in range(0, n):
        parts.append(arr[int(sen):int(sen + frac)])
        sen += frac

    return parts

def fileMaker(N,B): # number of files
    num = B  # num controls the number of elements to be sorted
    start = 1
    end = 1000000  # end controls the maximum size of one integer in the list
    targets = []
    
    for i in range(0, N):
        targets.append(open("RandomNumbers" + str(i), 'w'))  # Creates a file called "RandomNumbers"
    array = rand(start, end, num)  # Calls the rand() function

    parts = partition(array, N)

    i = 0

    for part in parts:
        for item in part:
            targets[i].write("%s\n" % item)  # Writes the random numbers into the file, line by line
        i += 1


def sorter(A,B):
    N =int(A)  # Number of cores
    print("Sorting a batch of numbers on " + str(N) + " cores : MultiCore Processing")
    startTime = time.time()
    batch = []  # for linear, the pool only contains 1 file

    for i in range(0, N):
        batch.append("RandomNumbers" + str(i))

    pool = Pool()
    ret = pool.map(sortfunc, batch)

    pool.close()
    pool.join()

    arrays = []

    for a in ret:
        arrays.append(a)

    endTime = time.time()

    print("Total time taken : " + str(endTime - startTime) + "seconds")

	# Put the run time results in a separate file with name including the number of files
    f = open("results"+ str(B) +".txt","a")
    f.write("Cores: "+str(N)+", Data: "+ str(B) +"\n")
    f.write("total time taken : " + str(endTime - startTime) + " seconds \n")
    f.close()

def delete():
    for i in range(-1, 9):
        if os.path.exists("RandomNumbers" + str(i)):
            os.remove("RandomNumbers" + str(i))


if __name__ == '__main__':

    N=int(input()) # Input the number of integers to be sorted
    k=1 #Tracks the number of files
    while(k<9): #Runs from 1 file to 8 files, essentially 1 core to 8 cores
        delete() #Deletes preexisting integer files
        fileMaker(k,N) # Creates N number of integers split into k files
        sorter(k,N) #sorts the k files using quicksort, the “N” is used to name the results file
        k=k+1 


