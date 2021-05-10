## Problem-3 Rearrange Array Digits

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:  ## edge case when the input list is either empty or of length =1.In this case return the input_list
        return input_list
    
    def heapify(input_list,length):  ## heapify function to convert the given input list into max heap
        
        for index in range(length):            
            parent_index = (index-1)//2        
            while parent_index > -1:
                if input_list[parent_index] < input_list[index]:
                    temp = input_list[parent_index]
                    input_list[parent_index] = input_list[index]
                    input_list[index] = temp
                    index = parent_index
                    parent_index = (index - 1)//2
                else:
                    break     
    
    heapify(input_list,len(input_list)) ## call heapify on the given input_list
    
    ## logic to calculate the number of digits in the 2 output numbers    
    if len(input_list) % 2 ==0:
        big_length = small_length = len(input_list)//2
    else:
        big_length = len(input_list)//2 + 1
        small_length = len(input_list) - big_length
    
    
    length = len(input_list) 
    ## initialize big number, small number
    big_number = 0              
    small_number = 0
    
    ## since the input list is max heapifyed.Extract the max element(element at index 0) and then heapify the remaining list
    ## again.Doing this for the entire length of the input list ensures that we are extracting elements in the descending order
    ## Every alternate element extracted contributes either to the big number or to the  small number
    ## Using the logic above to calculate the number of digits in each of the output number, we can multiply with the Power of
    ## 10 to calculate the final 2 numbers and return them as the list of 2 numbers
   
    for index in range(len(input_list)):
        
        first_element = input_list[0]
        input_list[0] = input_list[length-1]
        input_list[length-1] = first_element
        
        if index % 2 == 0:
            big_number += first_element*(10**(big_length-1))
            big_length -=1
        else:
            small_number += first_element*(10**(small_length-1))
            small_length -=1
            
        length -= 1
        heapify(input_list,length)
    
    return list([big_number,small_number])
        
        
        
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]    
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1], [1]])
test_function([[], []])
test_function([[1,3,2], [32,1]])
test_function([[4,6,0], [60,4]])
test_function([[0,1,4,6,0], [610,40]])
test_function([[1,1,1], [1,11]])
test_function([[0,0,0], [0,0]])
test_function([[0,1,2,3,4,5,6,7,8,9], [97531, 86420]])    

## Output from Jupyter Notebook

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

"""
