## Problem-1 LRU Cache

## import deque from collections module

from collections import deque

class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self._cache = {}               
        self._capacity = capacity               
        self._q = deque()                 ## instantiate queue to hold recent elements accesses in LRU cache

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        
        if key in self._cache:
            self._adjust_entries_in_queue(key)
            return self._cache[key]        
        return -1
        

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        
        if key in self._cache:    ## if key already exists,update its value with the new value
            self._cache[key] = value
            self._adjust_entries_in_queue(key)  # since the key is accessed, adjust entry in queue                   
              
        elif self.size() < self._capacity:  ## new key and the cache is not full          
            self._cache[key]= value         ## add the entry in cache
            self._adjust_entries_in_queue(key)    ## adjust the entry in queue        
        
        elif self.size() == self._capacity: ## new key and the cache is full
            element = self._q.pop()         ## evict least recently used element(key) from queue
            del self._cache[element]        ## delete corresponding key,value pair from the cache
            self._cache[key]= value         ## add a new key,value pair in the cache
            self._adjust_entries_in_queue(key) ## adjust entry in queue
                       
           
    def size(self):                      ## returns size of cache
        return len(self._cache)
    
           
    def _adjust_entries_in_queue(self,key): ## internal method
        
        """
        keeps track of recently used/added keys in a queue
        if key already exists it moves the key from its current postion to tail position
        if key is added,it goes to the end(tail) of the queue     
        
        """        
        if key in self._q:
            self._q.remove(key)
            self._q.appendleft(key)
        else:
            self._q.appendleft(key)
            