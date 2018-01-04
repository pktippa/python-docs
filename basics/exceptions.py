def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print(total)
    except:
        print("Some error occured")
    print("Returning back from function.")
    return total
     
list_of_values=[100,200,300,"400",500]
print("Total expenditure :", calculate_expenditure(list_of_values))

# Built in Exceptions
# ZeroDivisionError, TypeError, NameError, IndexError, ValueError
# Python also follows exception heirarchy same as like Java.


# If an error occurs inside a function and if the error is not caught inside it, 
# then the error is transferred to the function call where we have another opportunity to catch it.
def calculate_sum(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print("Total:",total)
        avg=total/no_values # This is where the NameError will be thrown.
        print("Average:",avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except TypeError:
        print("Wrong data type")

try:
    list_of_values=[100,200,300,400,500]
    num_values=len(list_of_values)
    calculate_sum(list_of_values)
except NameError:
    print("Name error occured")
except:
    print("Some error occured")

print()
# With Finally block
try:
    int_type = 10
    str_type = "A"
    combined = int_type + str_type
except TypeError:
    print("TypeError")
except:
    print("last except")
finally:
    print("in finally")