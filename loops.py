# While Loop
print("======While Loop=====")
baggage_count=4
while(baggage_count>0):
    baggage_count -= 1
    print("No. of baggage remaining:",baggage_count)

# For Loop
print("=======For Loop=======")
#  for loop allows the loop to run over a specific sequence of values
for number in 1,2,3,4:
    print("the current number is ", number)

# lets say you want to loop big range of values lets say 1 to 100
# we can use range(x,y,step) it creates a sequence from x to y-1 with a difference of step between each value. 

print("=====For loop Using Range=======")
for number in range(1,7,2):
    print ("The current number is ",number)

print("====== Using 'break' statement======")
for number in range(1,7,2):
    if number%3 == 0 :
        print("Number is divisible by 3 breaking the loop.")
        break
    print ("The current number is ",number)


print("====== Using 'break' statement======")
for number in range(1,7,2):
    if number%3 == 0 :
        print("Number is divisible by 3 continue to next iteration, not going to print the current number.")
        continue
    print ("The current number is ",number)
