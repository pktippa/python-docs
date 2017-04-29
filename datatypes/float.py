x=3 # Assigning a floating value number
y=2
z=x/y # Performing division to lead to a floating value
# 'round' function rounds the value to n decimal places.
print(round(z,2)) 
# where as round doesn't give trailing zeros if that is needed
print('{0:.2f}'.format(round(z,2)))

# Print to n decimals
# "{:.nf}".format(float)
float_val = 9.87897654
# Prints 9.879
print("{:.3f}".format(float_val))