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
a.union(b) # Values which exist in a or b
a.intersection(b) # Values which exist in a and b
a.difference(b) # Values which exist in a but not in b