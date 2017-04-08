flight_file=open("flight.txt","w")
flight_file.write("Hello")
text=flight_file.read()
flight_file.close()
flight_file.closed # Returns whether the file is closed or not.