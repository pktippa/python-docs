# Lambdas are functions without names, in other words they are anonymous functions. 
# They take inputs and return outputs but do not have a name. 
# They are shortcuts to create simple temporary functions.  

# Like functions Lambda expressions cannot have multiple statements
h = lambda x: x >40 and x< 50
print(h(45))
print(h(20))

def sum_all(function, data):
    result_sum=0;
    for w in data:
        if(function(w)):
            result_sum = result_sum+ w
    return result_sum

Q=[1,3,4,5,6,7,8,9,10,15,20]

p = lambda x:x

q = lambda x : x%2 == 0

r = lambda x : x%3 == 0


print(sum_all(p,Q))
print(sum_all(q,Q))
print(sum_all(r,Q))