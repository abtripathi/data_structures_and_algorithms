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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

## collect numbers which have only made outgoing calls
callers = set()
receivers = set()
for record in calls:
    callers.add(record[0])
    receivers.add(record[1])

number_send_or_receive_texts = set()
for record in texts:
    number_send_or_receive_texts.add(record[0])
    number_send_or_receive_texts.add(record[1])

only_callers = callers - receivers  # callers who have never received any calls

possible_telemarketers = only_callers - number_send_or_receive_texts

print("These numbers could be telemarketers: ", end='\n' * 2)
for item in sorted(possible_telemarketers):
    print(item)

"""
Run time analysis
O(1) time complexity for adding element in set and O(nlogn) for sorting in lexicographic order
O(n) space complexity

"""
