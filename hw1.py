import random
import time
import matplotlib.pyplot as plt

random.seed(10)

class SearchAlgorithms:
    def __init__(self):
        self.arr = []
        self.size = 0

    #generates an array of randomly generated numbers between -2^32 and 2^32 with no repeats
    def generate_array(self, size):
        self.arr = random.sample(range(-(2**32), 2**32), size)
        self.size = size
    
    def linear_search(self, array, target):
        i = 0
        while i < len(array):
            if array[i] == target:
                return i
            i += 1
        return -1
    
    def binary_search(self, array, target, low, high):
        n = high - low
        if n == 0:
            if array[low] == target:
                return low
            else:
                return -1
        else:
            mid = (low + high)//2
            if array[mid] < target:
                return self.binary_search(array, target, mid+1, high)
            else:
                return self.binary_search(array, target, low, mid)
    
    #times some number of linear searches on the same array
    def time_linear_search(self, num_searches, sort):
        if sort:
            self.arr = sorted(self.arr)
        startLS = time.time()
        for i in range(num_searches):
            randInd = random.randint(0, len(self.arr)-1)
            toFind = self.arr[randInd]
            self.linear_search(self.arr, toFind)
        endLS = time.time()
        executionLS = endLS - startLS
        return executionLS
    
    #times some number of binary searches on the same array
    def time_binary_search(self, num_searches, sort):
        startBS = time.time()
        if sort:
            self.arr = sorted(self.arr)
        for i in range(num_searches):
            randInd = random.randint(0, len(self.arr)-1)
            toFind = self.arr[randInd]
            self.binary_search(self.arr, toFind, 0, self.size-1)
        endBS = time.time()
        executionBS = endBS - startBS
        return executionBS

#runs from 1 up to 100 searches of an array using each search algorithm for 3 different sizes
test = SearchAlgorithms()
for n in [10, 30, 100]:
    test.generate_array(n)
    timesLS_US = []
    timesBS_US = []
    timesLS = []
    timesBS = []

    num_searches_range = range(1, 100)
    for i in num_searches_range:
        execution_time_LS_US = test.time_linear_search(i, False)
        timesLS_US.append(execution_time_LS_US)
        execution_time_BS_US = test.time_binary_search(i, False)
        timesBS_US.append(execution_time_BS_US)
        execution_time_BS = test.time_binary_search(i, True)
        timesBS.append(execution_time_BS)
        execution_time_LS = test.time_linear_search(i, True)
        timesLS.append(execution_time_LS)

    plt.figure(figsize=(10, 6))
    plt.plot(num_searches_range, timesBS, marker='o')
    plt.plot(num_searches_range, timesBS_US, marker='o')
    plt.plot(num_searches_range, timesLS_US, marker='o')
    plt.plot(num_searches_range, timesLS, marker='o')
    plt.legend(['Binary Search', 'Binary Search (unsorted array)', 'Linear Search', 'Linear Search (sorted array)'], loc = 'upper left')
    plt.xlabel('Number of Searches')
    plt.ylabel('Total Execution Time (seconds)')
    plt.title(f'Execution Time of Binary vs. Linear Search for Different Numbers of Searches on an Array of Size {test.size}')
    plt.grid (True)
    plt.show()

#generates arrays with sizes that are multiples of 1000 from 1 to 100000 and runs 10/50/100 searches on each array using each search algorithm
test2 = SearchAlgorithms()
for num_searches in [10, 50, 100]:
    timesLS2 = []
    timesBS2 = []
    timesLS_US2 = []
    timesBS_US2 = []

    sizes_range = range(1, 100000, 1000)
    for size in sizes_range:
        test2.generate_array(size)
        execution_time_LS_US = test2.time_linear_search(num_searches, False)
        timesLS_US2.append(execution_time_LS_US)
        execution_time_BS_US = test2.time_binary_search(num_searches, False)
        timesBS_US2.append(execution_time_BS_US)
        execution_time_BS = test2.time_binary_search(num_searches, True)
        timesBS2.append(execution_time_BS)
        execution_time_LS = test2.time_linear_search(num_searches, True)
        timesLS2.append(execution_time_LS)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes_range, timesBS2, marker='o')
    plt.plot(sizes_range, timesBS_US2, marker='o')
    plt.plot(sizes_range, timesLS_US2, marker='o')
    plt.plot(sizes_range, timesLS2, marker='o')
    plt.legend(['Binary Search', 'Binary Search (unsorted array)', 'Linear Search', 'Linear Search (sorted array)'], loc = 'upper left')
    plt.xlabel('Array Size')
    plt.ylabel('Total Execution Time (seconds)')
    plt.title(f'Execution Time of {num_searches} Binary Searches vs. {num_searches} Linear Searches on Different Sized Arrays')
    plt.grid (True)
    plt.show()