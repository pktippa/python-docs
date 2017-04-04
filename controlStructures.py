# if else elseif
ticket_status="Confirmed"
luggage_weight=32
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(ticket_status=="Confirmed"):
    if(luggage_weight>0 and luggage_weight<=weight_limit):
        print("Check-in cleared")
    elif(luggage_weight<=(weight_limit+10)):
        extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-weight_limit)  
    if(extra_luggage_charge>0):
        print("Extra luggage charge is Rs.", extra_luggage_charge)  
        print("Please make the payment to clear check-in")     
else:
    print("Sorry, ticket is not confirmed")


# Switch case is not there by default, but we can achieve using dictionary
#http://stackoverflow.com/a/11479840/3629379

# define the function blocks
def zero():
    print ("You typed zero.\n")

def prime():
    print("Prime")

# map the inputs to the function blocks, or building dictionary
options = {'zero' : zero, 'prime': prime}
options['zero']()  # Invoking the particular function and execute it.