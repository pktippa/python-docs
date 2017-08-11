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