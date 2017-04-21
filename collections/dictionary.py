# Creating a dictionary	
crew_details = { 
    "Pilot":"Kumar",
    "Co-pilot":"Raghav",
    "Head-Strewardess":"Malini",
    "Stewardess":"Mala" 
}

# Accessing the value using key	
print(crew_details["Pilot"])

# Iterating through the dictionary	
for key,value in crew_details.items():
     print(key,":",value)

# Built in Functions
crew_details={
              "Pilot":"Kumar",
              "Co-pilot":"Raghav",
              "Head-Strewardess":"Malini",
              "Stewardess":"Mala"
              }
crew_details.get("Pilot") # Returns the value for given key. If the given key is not found, returns None
crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"}) # Updates the dictionary with the given key-value pairs.     

# Get default value if the key,value pair doesnt exists
chef_name = crew_details.get('chef', 'Robin')