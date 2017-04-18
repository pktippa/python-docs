pancard_number="AABGT6715H"

#Length of the string
print("Length of the PAN card number:", len(pancard_number))

#Concatenating two strings
name1 ="PAN "
name2="card"
name=name1+name2
print(name)

print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
    print(pancard_number[index])
    
print("Iterating the string using keyword in")
for value in pancard_number:
    print(value)

print("Searching for a character in string")
if "Z" in pancard_number:
    print("Character present")
else:
    print("Character is not present")

#Slicing a string
print("The numbers in the PAN card number:", pancard_number[5:9])
print("Last but one 3 characters in the PAN card:",pancard_number[-4:-1])

# pancard_number[2]="A" #This line will result in an error, i.e., string is immutable
# print(pancard_number)

# Built in Functions for String
flightname = "Air India"
flightname.count("a")
flightname.replace("A", "a")
flightname.find("a")
flightname.startswith("Ai")
flightname.endswith("ia")
flightname.isdigit() # Checks whether the string contains all digits.
flightname.upper()
flightname.lower()
flightname.split("a")

# Multiple value mapping using split
given_string = "1 2 3 4 5"
first_num, *rest_of_nums_in_str = given_string.split()
rest_of_nums_in_int = list(map(int, rest_of_nums_in_str))
print(rest_of_nums_in_int)

print("=======================")
upper_lower_str = "AbC"
for s in upper_lower_str:
    print(s.isupper()) # String .isupper() returns if the character is upper or lower.

print("=========== Find Method ============")
string = "abcdabcd"
first_occurence_of_ab = string.find("ab") # Find always returns the first occurence of str if not index provided.
second_occurence_of_ab = string.find("ab", first_occurence_of_ab+1) # If you want to find the next occurence we can pass the index as (first occurence index + 1).
print("first ab ", first_occurence_of_ab , " second ab ", second_occurence_of_ab)

string.isalnum() # Checks whether the string contains all alphabets or numbers
string.isalpha() # Checks whether the string contains all alphabets or not.

# str.ljust(width) returns left aligned string of length width
# str.center(width) returns a centered string of length width.
# str.rjust(width) returns a right aligned string of length width.
print("======= Text Alignment =========")
width = 20
print('HackerRank'.center(width,'-'))
print('HackerRank'.ljust(width,'-'))
print('HackerRank'.rjust(width,'-'))

print("======= Text Wrap / Fill =========")
import textwrap
print(textwrap.wrap(string,3)) # The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
print(textwrap.fill(string,4)) # The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

print("======= String Formatting =========")
print('{: >{}}'.format("ss", 3))# Prints
#   ss
print('{: <{}}'.format("ss", 3)+"another string") # Prints
# ss  another string.

# Split the string with empty separator
string = "abcd"
string_with_empty_separated = list(string)

# Capitalizing a string
print(string.capitalize()) # Automatically capitalizes.