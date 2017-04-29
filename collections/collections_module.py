# importing required functions from collections
from collections import Counter, defaultdict, namedtuple

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

# The defaultdict tool is a container in the collections class of Python.
# It's similar to the usual dictionary (dict) container, but it has one difference:
# The value fields' data type is specified upon initialization.

# This specifies the value fields data type is as list
d = defaultdict(list)
# And you can perform operations on the value list by passing the key
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
# Prints 
# ('python', ['awesome', 'language'])
# ('something-else', ['not relevant'])
for i in d.items():
    print(i)

# collections.namedtuple()
# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

Point = namedtuple('Point','x,y')
# iniatilizing objects
pt1 = Point(1,2)
pt2 = Point(3,4)
# 1*3 + 2*4
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# Prints 11
print(dot_product)
# Another way of using namedtuple
Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# Prints Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(xyz)
# We can also access indivudual properties of object
# xyz.Class returns Y, so prints Y
print(xyz.Class)
