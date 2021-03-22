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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

"""
area_code = set()
for record in calls:
    if record[0].startswith('(080)'):  # caller from bangalore
        if record[1].find(' ') == -1:  # not a mobile
            if not record[1].startswith('('):  # not a fixed line
                area_code.add(record[1][:3])  # adding area code for telecommuter
            area_code.add(record[1][1:record[1].find(')')])  # adding area code for fixed line
        else:
            area_code.add(record[1][:4])  # adding a prefix for mobile number

print('The numbers called by people in Bangalore have codes:', end='\n' * 2)

# sorting in lexicographic order
for item in sorted(area_code):
    print(item)

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

print()

total_calls = list()
for record in calls:
    if record[0].startswith('(080)'):  # caller from bangalore
        if record[1].startswith('(080)'):  # calls made to bangalore
            total_calls.append('080')  # quick way to identify 080 in the total calls list
        else:
            total_calls.append(record[1])

print("{:.2f} percent of call from fixed lines in Bangalore are calls to other fixed lines in Bangalore." \
      .format(total_calls.count('080') / len(total_calls) * 100))


