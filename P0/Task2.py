"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
duration_dict = {} # dictionary to store total duration for any given number in the calls list
for record in calls:
    duration_dict[record[0]] = duration_dict.get(record[0],0) + int(record[3])
    duration_dict[record[1]] = duration_dict.get(record[1],0) + int(record[3])

phone_number_with_max_duration = max(duration_dict,key=duration_dict.get)

# print message
print("{} spent the longest time, {} seconds,on the phone during September 2016. ".format(phone_number_with_max_duration,
                                                                                          duration_dict[phone_number_with_max_duration]))

"""
Run time analysis
O(1) time complexity for dictionary get and set and O(nlogn) for sorting 
O(n) for space complexity

"""
