def insert_sort(array):
    for i in range(len(array)):
        index = i
        while array[index - 1] > array[index] and index - 1 >= 0:
            array[index-1], array[index] = array[index], array[index-1]
            index -= 1
    return array

'''import numpy as np
import time
array = np.random.rand(1000)
start = time.time()
insert_sort(array)
end = time.time()
print(end - start)
'''
array = [10, 17, 50, 7, 30, 24, 27]
print(insert_sort(array))
