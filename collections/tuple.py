# Tuple

# Like list, tuple can also store a sequence of elements but the value of the elements 
# cannot be changed. (i.e. tuples are IMMUTABLE). Elements can be homogeneous or heterogeneous 
# but they are READ-ONLY.

sample_tuple = ("Denver", "Knight", "Larson")
# () are optional, a set of values separated by comma is also considered to be a tuple.
print("Second element in ", sample_tuple[1]) # Returns Knight

# Addition in tuples
tuple1 = (3,4,5)
tuple2 = tuple1 + (8,9) # We can also assign it to tuple1 which will override previous tuple.
print(tuple2) # Prints (3, 4, 5, 8, 9)

# Convert tuple of characters into string
str_tuple = ('R','o','y')
print(''.join(str_tuple)) # Prints Roy