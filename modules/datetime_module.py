import datetime
first_time_str = 'Sat 02 May 2015 19:54:36 +0530'
# Getting the second time string
second_time_str = 'Fri 01 May 2015 13:54:36 +0000'
# Converting into datetime format 
first_time = datetime.datetime.strptime(first_time_str, "%a %d %b %Y %H:%M:%S %z")
second_time = datetime.datetime.strptime(second_time_str, "%a %d %b %Y %H:%M:%S %z")
# Calculating the timedelta 
time_diff_seconds = datetime.timedelta.total_seconds(first_time - second_time)
# Converting to int and printing in absolute format.
# Prints 88200
print(abs(int(time_diff_seconds)))