"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# set to store different phone numbers
diff_phone_numbers = set()
for record in texts:
    diff_phone_numbers.add(record[0])
    diff_phone_numbers.add(record[1])
for record in calls:
    diff_phone_numbers.add(record[0])
    diff_phone_numbers.add(record[1])

# print message
print("There are {} different telephone numbers in the records".format(len(diff_phone_numbers)))


