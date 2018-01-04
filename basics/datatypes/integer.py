# a,b,c,d as 9, 29, 7, 27
# after calculation of a**b + c**d leads to 
# 4710194409608608369201743232 which wont fit in long long int of C++ or a 64-bit integer.
# but Python can store this number as integer
a,b,c,d = 9,29,7,27
print(a**b + c**d)