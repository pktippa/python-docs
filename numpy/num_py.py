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