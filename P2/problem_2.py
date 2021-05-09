## Problem-2 search in a rotated sorted array

def rotated_array_search(input_list, number):
    
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list)==0: ## check if input list is empty, return -1
        return -1
    
    ## recursive function  which uses binary search algorithm to search a target number in a sorted list
    def recursive_array_search(input_list,start_index,end_index,number):
        
        if start_index > end_index: ## base case of recursion
            return -1
        midpoint = (start_index+end_index)//2
        if input_list[midpoint] == number:
            return midpoint
        if input_list[midpoint] > number:
            return recursive_array_search(input_list,start_index,midpoint-1,number)
        else:
            return recursive_array_search(input_list,midpoint+1,end_index,number)
    
    ## retrieve the index of the greatest number in a rotated sorted array
    largest_number_index = find_index_of_largest_number(input_list) 
    
    ## return the index of the largest number if it matches the target number
    if input_list[largest_number_index] == number:
        return largest_number_index
    
    ## call search on the list of elements to the left of the greatest number
    left_search = recursive_array_search(input_list,largest_number_index+1,len(input_list)-1,number)
    
    ## call search on the list of elements to the right of the greatest number
    right_search = recursive_array_search(input_list,0,largest_number_index-1,number)
    
    ## return the index,if the target number is present else returns -1
    return right_search if right_search !=-1 else left_search 
        
    
def find_index_of_largest_number(input_list):
    
    ## function to retrieve the index of the largest number.This is called recursively
    def recursive_search_index(input_list,first_element,start_index,end_index):
        
        ## base case of recursion
        if start_index == end_index and input_list[start_index] >= first_element: 
            return start_index
        if start_index == end_index and input_list[start_index] < first_element:
            return start_index-1
        if end_index < start_index:
            return end_index

        midpoint = (start_index+end_index)//2
        ## recursively call the function on the list of elements to the right of midpoint
        if input_list[midpoint] > first_element:
            return recursive_search_index(input_list,first_element,midpoint+1,end_index)
        else:
             ## recursively call the function on the list of elements to the left of midpoint
            return recursive_search_index(input_list,first_element,start_index,midpoint-1)
        
    return recursive_search_index(input_list,input_list[0],0,len(input_list)-1)
    
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6],6 ])
test_function([[6],0 ])
test_function([[],0 ])
test_function([[],-1 ])
test_function([[],10 ])

## Result copied from Jupyter Notebook

"""
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass
Pass

"""
    