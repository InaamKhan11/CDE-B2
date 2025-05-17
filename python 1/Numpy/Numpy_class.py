"""
big O
time complexity
space complexity


Big O Notation
Big O notation is a mathematical notation used to describe the upper bound of an algorithm's time or space complexity. It provides a way to express how the runtime or memory usage of an algorithm grows relative to the input size.
Big O notation is used to analyze the performance of algorithms and to compare their efficiency. It helps in understanding how an algorithm will scale with larger inputs.
Big O notation is expressed as O(f(n)), where f(n) is a function that describes the growth rate of the algorithm's time or space complexity. The "O" stands for "order of," and it indicates that we are interested in the upper bound of the function.


"""

import numpy as np

height = [4.5, 5.2, 5.6, 6.3, 7.1, 5.8]

weight = [100, 98, 67, 71, 88, 77]


np_height = np.array([4.5, 5.2, 5.6, 6.3, 7.1, 5.8])

np_weight = np.array([100, 98, 67, 71, 88, 77])

bmi = np_weight / np_height ** 2

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

a = list1 + list2 # merge elements like append
# print(a)

np_list1 = np.array([1, 2, 3, 4, 5])
np_list2 = np.array([6, 7, 8, 9, 10])

b = np_list1 + np_list2 # sun elements 

# print(b)

# print(np_list1[np_list1 > 6])

# print(np_list2 > 6)


arr_2d = np.array([[1,2], [3,4], [5,6]])
# print(arr_2d[1, 0]) # access element at row 1, column 0
# print(arr_2d[1]) # access row 1
# print(arr_2d[1:])
# print(arr_2d[0: 2]) # access column 1
# print(arr_2d[2,0]) # access column 1

arr_3d = np.array([[[3,4], [5,6]], [[11,12], [20,22]]])
# print(arr_3d[0, 1, 0]) # access element at row 0, column 1, depth 0
# print(arr_3d[1,1,1]) # access row 0, column 1


# s = np_list1.shape
# s = np_list2.size
# s = np_list1.dtype
# s = np_list1.ndim

print(np.zeros((3, 4))) # create a 3x4 array filled with zeros
# print(np.ones((3, 4))) # create a 3x4 array filled with ones
# print(np.empty((3, 4))) # create a 3x4 array filled with random values
# print(np.arange(0, 10, 2)) # create an array with values from 0 to 10 with a step of 2
# print(np.linspace(0, 10, 5)) # create an array with 5 values evenly spaced between 0 and 10
# print(np.eye(3)) # create a 3x3 identity matrix
# print(np.random.rand(3, 4)) # create a 3x4 array with random values between 0 and 1
# print(np.random.randn(3, 4)) # create a 3x4 array with random values from a standard normal distribution
# print(np.random.randint(0, 10, (3, 4))) # create a 3x4 array with random integers between 0 and 10
# print(np.random.choice([1, 2, 3, 4, 5], size=(3, 4))) # create a 3x4 array with random values from the given list




np.mod(np_list2)

# print(s)
