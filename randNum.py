import random  # importing a library which gives additional functionality


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


# Main program
N = 1  # number of files
num = 10  # num controls the number of elements to be sorted
start = 1
end = 10000000  # end controls the maximum size of one integer in the list
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











