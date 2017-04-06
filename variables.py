# if you want to change a global variable value inside a function then specify it using 'global' keyword.

age = 10
def changeAge(newAge):
    global age
    age = newAge
changeAge(15)
print("new Age ", age)

# Python uses pass by reference technique.
# In Python, even when using pass by reference whether an argument gets
# modified or not depends on whether the variable type is mutable or not.
# In the below example weight_limit is immutable, so even when it is passed
# by reference the value doesn't change.
def change_weight_limit(wgt_limit):
    wgt_limit = 25
    print("Inside function:",wgt_limit)


weight_limit=30
print("Current weight limit:",weight_limit)
change_weight_limit(weight_limit)
print("New weight limit:",weight_limit)

# Pass by reference for mutable variables. Ex: List

def change_airline(airlines,new_airline):
    airlines[1]=new_airline

airline_list=["AirIndia","Emirates"]
print("Current list of airlines operating from the airport:", airline_list)

change_airline(airline_list,"Singapore Airlines")
print("Updated list of airlines operating from the airport:", airline_list)
