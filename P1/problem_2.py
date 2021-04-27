## Problem-2 File recursion

## import os module
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    filenames=[]
    if os.path.exists(path): ## check whether path exists
        for item in os.listdir(path):    ## scan current path    
            if os.path.isdir(os.path.join(path,item)):  ## if the item in the current path is a dir, recursively call find_fles   
                filenames.extend(find_files(suffix,os.path.join(path,item))) ## add items from recursive call 
            ## check if an item is a file which ends with a given suffix    
            elif os.path.isfile(os.path.join(path,item)) and os.path.join(path,item).endswith(suffix):                         
                    filenames.append(os.path.join(path,item))  
                
        return filenames
    return "Path doesn't exist"