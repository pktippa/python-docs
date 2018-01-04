import re
re.search(r"Air","Airline") # Air Contains anywhere in the String.
re.search(r"A..l","Aopline") # '.' stands for any character. In the example here it is any two characters.
re.search(r"A\dl","A2line") # \d stands for any digit. Here any digit found in between A and l
re.search(r"A\d*","A2234line") # Check if number is found 0 or n times.
re.search(r"A\d+","Airline") # Check if number is found 1 or n times, here the pattern result is not found.
re.search(r"A\d?i","Airline") # check if number is found 0 or 1 time, pattern result is found.
re.search(r"A\d{3}i","A223irline") # check exactly 3 digits are found after A, pattern result is found.
# here the pattern is not found. But [] does a single character substitution, we can specify sequence of values.
re.search(r"A[4-8]l","A2line") 
re.search(r"Hell|Fell","Fellow") # '|' acts as 'or' operator.
re.search(r"Air\s","Airline") # \s stands for space, here the pattern result is not found.
re.search(r"^A","Airline") # To check if a given string starts with A, pattern found
re.search(r"e$","Airline") # To check with given String ends with e, pattern found.
re.search(r"\w$","Airline%") # To check whether last character is alphanumeric a-z,A-Z,0-9,_ or not, pattern not found.

flight_details="Flight Savana Airlines a2134"
# To replace Flight with Plane
new_flight_details=re.sub(r"Flight",r"Plane",flight_details)
print(new_flight_details)
# () is used to group characters. Here we are grouping 4 numbers 
# together and referring it as \1. 1 indicates in first group.
print(re.sub(r"a(\d{4})",r"A\1",flight_details))
