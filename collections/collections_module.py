# importing required functions from collections
from collections import Counter, defaultdict, namedtuple, OrderedDict, deque

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

# collections.OrderedDict
# An OrderedDict is a dictionary that remembers the order of the keys that were 
# inserted first. If a new entry overwrites an existing entry, the original insertion 
# position is left unchanged.
ordered_dictionary = OrderedDict()
ordered_dictionary['a'] = 1
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
# We can use .get('el', default_value) to get or initialize a value if not exists.
ordered_dictionary['d'] = ordered_dictionary.get('d', 5)
# Prints OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 5)])
print(ordered_dictionary)
# we can loop through elements in OrderedDict using OrderedDict.keys() value by OrderedDict[key]
string = "pradeep"
# we can get the unique characters of a string using OrderedDict preserving the order.
# Prints prade
print(''.join(OrderedDict.fromkeys(string).keys()))

# collections.deque()
# A deque is a double-ended queue. It can be used to add or remove elements from both ends.
# Deques support thread safe, memory efficient appends and pops from either side of the deque
# with approximately the same O(1) performance in either direction.
d = deque()
d.append(1)
# Prints deque([1])
print(d)
d.appendleft(2)
# Prints deque([2, 1])
print(d)
d.clear()
# Prints deque([])
print(d)
d.extend('1')
# Prints deque(['1'])
print(d)
d.extendleft('234')
# Prints deque(['4', '3', '2', '1'])
print(d)
# Returns 1
d.count('1')
# Returns '1'
d.pop()
# Prints deque(['4', '3', '2'])
print(d)
# Returns '4'
d.popleft()
# Prints deque(['3', '2'])
print(d)
d.extend('7896')
# Prints deque(['3', '2', '7', '8', '9', '6'])
print(d)
d.remove('2')
# Prints deque(['3', '7', '8', '9', '6'])
print(d)
d.reverse()
# Prints deque(['6', '9', '8', '7', '3'])
print(d)
d.rotate(3)
# Prints deque(['8', '7', '3', '6', '9'])
print(d)