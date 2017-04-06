# Start of calculate Sum function
def calculate_sum (num1, num2) :
    return num1+num2
# End of function

sumOfValues = calculate_sum(10, 11)
print("Sum of values ", sumOfValues)

def display(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)

# Positional Arguments
display("AI789",200)

# display("EM333") # this gives error since the number of arguments expected by function doesn't match the arguments passed.

# Keyword Arguments
# we can pass arguments in any order by specifying the keywords of argument names
display(seating_capacity=250,flight_number="EI990")

# Default Arguments, if an argument wanted to set a default value if the value doesnt passed during the call.
def display2(flight_number, seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)

display2("AI789",250)

display2("EM333")

# Variable number of arguments
# any argument name preceded by '*' is considered to be a varying length tuple
def vending_machine(name, *item_code_tuple):
    print()
    print(name,"is provided:")
    for item_code in item_code_tuple:
        if item_code==12: print("Soft drink")
        elif item_code==15: print("Candy")
        elif item_code==11: print("Snack packet")
        elif item_code==13: print("Biscuit packet")
        else: print("Invalid item code")

vending_machine("Uday",12,15,13)
vending_machine("Raj",12,11)
