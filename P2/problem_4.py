## Problem-4 Dutch National Flag Problem

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    
   # Traverse the list from the beginning with index = 0.If the element is 2, swap it with the last element and decrement last 
   # index by 1.if the element is 0,swap it with the element at the next available position of 0,increment the next available
   # position of 0 by 1 and also the index by 1
   # if element is neither 2 or 0 meaning 1 then simply advance the index by 1
   # repeat until index crosses the last index meaning index > last index
   # Return the sorted inputlist as output

    next_pos_0,index = 0,0    
    last_index = len(input_list)-1
    while index <= last_index:
        if input_list[index]==2:            
            input_list[index] = input_list[last_index]
            input_list[last_index] = 2
            last_index -= 1        
        elif input_list[index] == 0:
            input_list[index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0            
            next_pos_0 +=1
            index += 1        
        else:
            index += 1
            
    return input_list
           
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
        
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0])
test_function([])
test_function([0,0,0])
test_function([0,1,2])
test_function([2,2,2])
test_function([2,0,0])
test_function([0,1,2,0,1,2])
test_function([0,2,1,0,1,2])
test_function([0,0,1,1,0,0,2,2])        

##########################################
# output as generated in Jupyter Notebook
##########################################

"""
[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
Pass
[0]
Pass
[]
Pass
[0, 0, 0]
Pass
[0, 1, 2]
Pass
[2, 2, 2]
Pass
[0, 0, 2]
Pass
[0, 0, 1, 1, 2, 2]
Pass
[0, 0, 1, 1, 2, 2]
Pass
[0, 0, 0, 0, 1, 1, 2, 2]
Pass

"""
