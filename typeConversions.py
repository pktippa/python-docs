# Using explicit converstions
numInStr = "10"
num2 = 11
numInInt = int(numInStr) # Conversion of String to Int
num3 = num2 + numInInt
print("Sum of numbers after explicit conversion ", num3)

newNumInInt = 25
ageStr = "Age : "
newNumInStr = str(newNumInInt) # Conversion of Int to Str
newNumInStr = ageStr + newNumInStr
print("After int to str explicit conversion and concatination  - ", newNumInStr)