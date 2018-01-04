# Set
#Removes the duplicates from the given group of values to create the set.
flight_set = {500,520,600,345,520,634,600,500,200,200}
print("Flight Set : ", flight_set)

# Converting List into Set
passengers_list=["George", "Annie", "Jack", "Annie", "Henry", "Helen", "Maria", "George", "Jack", "Remo"]
unique_passengers=set(passengers_list)#	set function - removes the duplicates from the list and returns a set

print("Unique Passengers : ", unique_passengers)

# Set can also contain any data types, even tuples are also allowed.
# Add function .add()
unique_passengers.add("Robin")

# .update() function works only for iterable objects
unique_passengers.update(["Rahul", "Robin"])
unique_passengers.update({"Kanvi", "Beatriz"})

# Both the discard() and remove() functions take a single value as an argument and
# removes that value from the set. If that value is not present, discard() does nothing,
# but remove() will raise a KeyError exception.
unique_passengers.discard("Annie")
unique_passengers.remove("George")

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
a.union(b) # Values which exist in a or b, we can also use a | b
a.intersection(b) # Values which exist in a and b, we can also use a & b
a.difference(b) # Values which exist in a but not in b, we can also use a - b
a.symmetric_difference(b) # Values of a and b but not common to both. we can also use a ^ b

# Check element existence in Set
el = 4
if el in a:
    print('element exists ', el)

# Intializing an empty Set
empty_set = set([])

# .pop() operation removes and return an arbitrary element from the set.
# If there are no elements to remove, it raises a KeyError.
ret_el = a.pop()

# We can directly call sum() function on set to get the sum of all elements.
sum_of_elements_of_a = sum(a) 

# Get the count of number of elements in the Set
set_elements_count = len(a)

# Set Mutations
# .update() or |=
a.update(b) # Which will add elements of b into a i.e update elements of a with b.
# .intersection_update() or &=
a.intersection_update(b) # Same as intersection but it will update the elements of a.
# .difference_update() or -=
a.difference_update(b) # Same as difference but it will update the elements of a.
# .symmetric_difference_update() or ^=
a.symmetric_difference_update(b) # Same as symmetric_difference but it will update the elements of a.

# Checking whether set A is subset of B
a.issubset(b)

# Checking whether set A is superset of B
a.issuperset(b)