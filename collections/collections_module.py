# importing required functions from collections
from collections import Counter

# collections.Counter() 
# A counter is a container that stores elements as dictionary keys, 
# and their counts are stored as dictionary values.
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# Prints Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
print(Counter(myList))
# Prints dict_items([(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)])
print(Counter(myList).items())
# Prints dict_keys([1, 2, 3, 4, 5])
print(Counter(myList).keys())
# Prints dict_values([3, 4, 4, 2, 1])
print(Counter(myList).values())
c = Counter(myList)
c[2] = 5
print(c)
print(Counter(myList))