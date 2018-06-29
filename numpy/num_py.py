# All basic usage of numpy
import numpy as np
# prints the version of numpy
print(np.__version__)

# Whether element is a numpy array
el = np.array(list())
# Below command resolves to true
if isinstance(el, np.ndarray):
    print("Element is a numpy array.")

array1 = np.array([1, 2, 3, 4])
# It performs element wise operation on whole collection
sum_of_array = array1 + array1
# Returns [2, 4, 6, 8]
print(sum_of_array)

# We can access individual numpy array elements, use square brackets
# Prints 2. i.e. value of array with index 1
print(array1[1])
# Returns array of boolean values which are greater than 2
array2 = array1 > 2

# Prints [False, False, True, True]
print(array2)
# We can print selective items of array by passing array of boolean values
array3 = array1[array2]
print(array3)

two_d_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
two_d_array = np.array(two_d_list)
# Shape is 3 rows, 4 columns
print(two_d_array.shape)
# To get all the 3rd columns of 
print(two_d_array[:,2])
# To get values [6, 7]
print(two_d_array[1,1:3])

# Reshape
org_array = [1, 2, 3, 4, 5, 6, 7, 8]
conv_np_array = np.array(org_array)
# Returns (8,) as shape
print('Shape ', conv_np_array.shape)
# Converting into shape of (2,4)
conv_2_4_array = np.reshape(conv_np_array, [2, 4])
# Returns (2, 4) as shape
print('Shape ', conv_2_4_array.shape)
# Prints [[1 2 3 4], [5 6 7 8]]
print('Element of conv_2_4_array', conv_2_4_array)
# Converting into shape of (2, 2, 2)
conv_2_2_2_array = np.reshape(conv_np_array, [2, 2, 2])
# Returns (2, 2, 2) as shape
print('Shape ', conv_2_2_2_array.shape)
# Prints
"""
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
"""
print('Element of conv_2_2_2_array', conv_2_2_2_array)

# The shape will convert [row1, row2, ....rown-1, col]
# If we want to have single row with elements just 1 or -1 to the top of the shape list.

# Converting into shape of (1, 2, 2, 2)
conv_1_2_2_2_array = np.reshape(conv_np_array, [-1, 2, 2, 2])
# Returns (1, 2, 2, 2) as shape, even if we gave first dimension of shape as -1
print('Shape ', conv_1_2_2_2_array.shape)
"""
[[[[1 2]
   [3 4]]

  [[5 6]
   [7 8]]]]
"""
print('Element of conv_1_2_2_2_array', conv_1_2_2_2_array)

# Perform an operation on each element of array
"""
import math
import numpy as np

def calcSigmoid(z):
    return 1 / ( 1 + math.exp(-z) )

def sigm(X):
    sm = np.vectorize(calcSigmoid)
    return sm(X)

sigm([1,0])
array([0.73105858, 0.5       ])
"""

# Adding columns

first = np.array([[1,3], [2,4]])
'''
array([[1, 2],
       [3, 4]])
'''

sec = np.array([[5],[6]])
'''
array([[5],
       [6]])
'''

# on column concat
third = np.concatenate((first, sec), axis=1)
'''
array([[1, 2, 5],
       [3, 4, 6]])
'''

# Get the scalar value of (1,1) matrix
in_vec = np.array([[5]])
'''
array([[5]])
'''
in_vec.shape # (1, 1)
in_scalar = np.asscalar(in_vec) # 5

# identity matrix
eye = np.eye(3)
'''
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
'''

# Reading csv file
'''
from numpy import genfromtxt
my_data = genfromtxt('my_file.csv', delimiter=',')
'''

'''
X = np.arange(1,7)
#array([1, 2, 3, 4, 5, 6])
X = X.reshape(3, 2)

array([[1, 2],
       [3, 4],
       [5, 6]])

If we see the elements arranged in filling first rows by rows
If we want to fill by columns first, i.e

array([[1, 4],
       [2, 5],
       [3, 6]])


We can do in two ways

1. First take the order in reverse then transpose

X = np.arange(1,7).reshape(2,3) # Observe 2,3 rather thn 3,2
X = X.T

2. Chaining with swapaxes

X = np.arange(1,7).reshape(2,3).swapaxes(0,1)
'''

'''
Indexing from particular index to end
mm = np.arange(1,5).reshape(2,2)
mm
array([[1, 2],
       [3, 4]])
nn = mm.flatten().reshape((4,1))
array([[1],
       [2],
       [3],
       [4]])
# From index 2 to end
nn[2:,]
array([[3],
       [4]])