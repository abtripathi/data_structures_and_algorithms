## Problem-6 Max and Min in an Unsorted Array

def get_min_max(ints):
    
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
   
    
    if len(ints) == 0: ## edge case when the list passed is empty,return empty tuple
        return tuple()   
    
    ## assign first element to be both maximum and minimum
    
    maximum = ints[0] 
    minimum = ints[0]
    
    ## Iterate from 2nd element to the end of the list and modify maximum,minimum variable by comparing them to the elements 
    ## accessed during traversal
    
    for index in range(1,len(ints)):
        if ints[index] > maximum:
            maximum = ints[index]
        if ints[index] < minimum:
            minimum = ints[index]
            
    return minimum,maximum
    
    
    
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9

random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

## Output as displayed in Jupyter notebook

"""
Pass

"""
## Edge test case

l = []

print ("Pass" if () == get_min_max(l) else "Fail")

## Output as displayed in Jupyter notebook

"""
Pass

"""


## Edge test case

l = [1]

print ("Pass" if (1,1) == get_min_max(l) else "Fail")

## Output as displayed in Jupyter notebook

"""
Pass

"""


## Edge test case

l = [0]

print ("Pass" if (0,0) == get_min_max(l) else "Fail")

## Output as displayed in Jupyter notebook

"""
Pass

"""

## Edge test case

l = [2,2]

print ("Pass" if (2,2) == get_min_max(l) else "Fail")

## Output as displayed in Jupyter notebook

"""
Pass

"""