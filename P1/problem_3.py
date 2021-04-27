## Problem-3 Huffman coding

from functools import total_ordering
import sys

## defining Node class


## total_ordering is used to define compare methods for the purpose of comaring nodes while putting them 
## in priority queue

@total_ordering     
class Node:
    def __init__(self,data,frequency):
        self.data = data
        self.frequency = frequency
        self.left_child = None
        self.right_child = None
        
    def get_frequency(self):
        return self.frequency    
    
    def set_data(self,data,frequency):
        self.data= data
        self.frequency = frequency
        
    def get_data(self):
        return self.data
        
    def set_left_child(self,node):
        self.left_child = node
        
    def set_right_child(self,node):
        self.right_child = node
        
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def has_right_child(self):
        return self.right_child !=None
    
    def has_left_child(self):
        return self.left_child !=None 
    
    def __eq__(self,other):
        
        if other !=None:
            return self.frequency==other.frequency
        return False
    
    def __lt__(self,other):
        return self.frequency < other.frequency
    
    def __gt__(self,other):
        return self.frequency > other.frequency
        
    def __str__(self):
        return "Node({},{})".format(self.data,self.frequency)
    
    def __repr__(self):
        return "Node({},{})".format(self.data,self.frequency)
        
        import heapq

## priority queue wrapper class using heapq module
class PriorityQueue:    
    def __init__(self,init_list=None):
        
        if init_list !=None:
            heapq.heapify(init_list)
            self.heap = init_list
        else:
            self.heap=[]
        
    def put(self,item):
        heapq.heappush(self.heap,item)
        
    def get(self):        
        if self.size() !=0:
            return heapq.heappop(self.heap)
        return None
    
    def top(self):
        if self.size() !=0:
            return self.heap[0]
        return None
    
    def size(self):
        return len(self.heap)
        
        ## huffman encoding

from collections import Counter


def huffman_encoding(data):
    
    """     
     encode data using huffman encoding scheme   
    
    """
    
    root = build_huffman_tree(data)  ## call function to build huffman tree
    
    if root is None:
        return '',None
    
    
    encoded_dict = traverse_to_get_encoded_value(root) ## get the bit sequence mapping
    
    #print(encoded_dict)
    
    return ''.join([encoded_dict[letter] for letter in data]),root ## return encoded data and root node
    
def build_huffman_tree(data):
    
    ## get the unique letters and their frequency from data.Assumption here is that data is string and hence iterable 
    frequency_dict = dict(Counter(data)) 
    
    ## if there is only one kind of letter in data, add a dummy character so that huffman tree can be built
    if len(frequency_dict)==1:  
        frequency_dict['<end>']=1
    if len(frequency_dict) == 0:
        return None
        
    ## prepare and add the data in a priority queue
    list_of_nodes = [ Node(letter,freq) for letter,freq in frequency_dict.items()]
    
    #print(list_of_nodes)
    
    pq = PriorityQueue(list_of_nodes)        
    while True:
        if pq.size()==1:
            new_node = pq.get()
            break
        node_1 = pq.get() # pop first min element
        node_2 = pq.get() # pop second min element
        new_node = Node('',node_1.get_frequency()+node_2.get_frequency()) ## create new node
        if node_1.get_frequency() <= node_2.get_frequency():
            new_node.set_left_child(node_1)
            new_node.set_right_child(node_2)
        else:
            new_node.set_left_child(node_2)
            new_node.set_right_child(node_1)
        pq.put(new_node)
    
    return new_node


def traverse_to_get_encoded_value(node):
    
    encoded_mapping = dict()  ## create an empty dictionary to get the bit sequence mapping
    
    ## call function recursively
    def _traverse_to_get_encoded_value(node,encoding): 
        
        if node.has_left_child():
            _traverse_to_get_encoded_value(node.get_left_child(),encoding +'0')      
        
        if node.has_right_child():            
            
            _traverse_to_get_encoded_value(node.get_right_child(),encoding +'1')
            
        if node.get_data():
            encoded_mapping[node.get_data()]=encoding
            
    _traverse_to_get_encoded_value(node,'')
    
    return encoded_mapping
    
    
def huffman_decoding(data,tree):
    
    """
     to decode huffman encoded data
     
    """
    if tree is None:
        return ''
    decoded_value = ''
    node = tree
    for bit in data:        
        if not node.has_left_child() and not node.has_right_child():            
            if node.get_data():
                decoded_value += node.get_data()                
            node = tree                
        if bit=='0':
            node = node.get_left_child()
        else:
            node = node.get_right_child()    
            
    ## extra check for the last iteration not covered in the loop
    if not node.has_left_child() and not node.has_right_child():
        if node.get_data():
            decoded_value += node.get_data()        
            
    return decoded_value
        
        


## test harness
def test_function(test_cases):
    
    print("Summary\n")
    print("-"*127,)
    print()
    
    for index,test_case in enumerate(test_cases,1):
        
        encoded_data = huffman_encoding(test_case[0])
        print("Test-case {}\n".format(index))
        
        
        if encoded_data[0]== test_case[1]:
            print('Huffman Encoding -> Pass\n')
        else:
            print('Huffman Encoding -> Fail\n')
        decoded_data = huffman_decoding(test_case[1],encoded_data[1])
        if decoded_data == test_case[0]:
              print('Huffman Decoding -> Pass\n')
        else:
              print('Huffman Decoding -> Fail\n')
        
        print ("The size of the data is: {}\n".format(sys.getsizeof(test_case[0])))
        print ("The content of the data is: {}\n".format(test_case[0]))
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data[0], base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data[0]))
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))
        print("-"*127)
        print()