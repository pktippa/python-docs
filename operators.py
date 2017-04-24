# Arthmetic Operators.
num1 = 11
num2 = 5
sumOfNums = num1 + num2
subtractOfNums = num1 - num2
multiplyOfNums = num1 * num2
divisionOfNums = num1 / num2
modulusOfNums = num1 % num2
integerDivisionOfNums = num1 // num2

print("======= Arthmetic Operators ==========")
print("Sum + of ", num1, " and  ", num2 , " is : ", sumOfNums)
print("Subrtraction - of ", num1, " and  ", num2 , " is : ", subtractOfNums)
print("Multiplication * of ", num1, " and  ", num2 , " is : ", multiplyOfNums)
print("Division / of ", num1, " and  ", num2 , " is : ", divisionOfNums)
print("Modulus % of ", num1, " and  ", num2 , " is : ", modulusOfNums)
print("Integer Division // of ", num1, " and  ", num2 , " is : ", integerDivisionOfNums)

print("======= Relational Operators ==========")
if num1 == num2 :
    print("== operator num1 and num2 are equal")
else :
    print("== operator num1 and num2 are not equal")

if num1 != num2 :
    print("!= operator num1 and num2 are not equal")
else :
    print("!= operator num1 and num2 are equal")

if num1 > num2 :
    print("> operator num1 is greater than num2")

if num1 < num2 :
    print("< operator num1 is less than num2")
else :
    print("< operator num1 is not less than num2")

if num1 >= num2 :
    print(">= operator num1 is greater than or eqaul to num2")

if num1 <= num2 :
    print("<= operator num1 is less than or equal to num2")
else :
    print("<= operator num1 is not less than or eqaul to num2")

print("======= Assignment Operators ==========")
print("= operator num1 is assigned to ", num1, "num2 to ", num2)

num1 += num2
print("+= operator num1 has changed value to ", num1)

num1 -= num2
print("-= operator num1 has changed value to ", num1)

num1 *= num2
print("*= operator num1 has changed value to ", num1)

num1 /= num2
print("/= operator num1 has changed value to ", num1)

num1 %= num2
print("%= operator num1 has changed value to ", num1)

print("======= Logical Operators ==========")
bool1 = True
bool2 = False

bool3 = bool1 and bool2
print("Logical 'and' operator between bool1 and bool2 ", bool3)

bool3 = bool1 or bool2
print("Logical 'or' operator between bool1 and bool2 ", bool3)

bool3 = not bool1
print("Logical 'not' operator on bool1", bool3)

# Power of shortcut
x = 4
print(4**3) # Returns 64 i.e. 4*4*4 or 4 power of 3