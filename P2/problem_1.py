## Problem-1 Square root of an Integer

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root       
    """
    if isinstance(number,int):
        ## seed call with lower bound as 1,upper bound as original number divided by 2
        return recursive_root(1,number,number)
    
    return "Number is not Integer"
   

def recursive_root(lower_bound,upper_bound,number):
    
    midpoint = (lower_bound+upper_bound)//2 ## finding the midpoint
    
    if midpoint == lower_bound: ## base case happens when lower and upper bound are contiguous numbers for e.g 20,21 or 45,46
        return midpoint
    
    if  midpoint**2 == number: ## if we actually hit the midpoint which is the real root(no decimals) of the given number 
        return midpoint
    
    elif midpoint**2 < number: #    
        return recursive_root(midpoint,upper_bound,number) ## recursively call by increasing he lower bound    
    
    else:
        return recursive_root(lower_bound,midpoint,number) ## recursively call by decreasing the upper bound    
        