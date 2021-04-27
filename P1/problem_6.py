## Problem-6 Union and Intersection

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def to_list_of_values(self):
        value_list = []
        node = self.head
        while node:
            value_list.append(node.value)
            node = node.next
        return value_list  
        

    def size(self):
        return len(self.to_list_of_values()) 

def union(llist_1, llist_2):
   
    llist_1_values = llist_1.to_list_of_values()    
    llist_2_values = llist_2.to_list_of_values()   
    union_elements = set(llist_1_values+llist_2_values)
    llist_3 = LinkedList()
    for element in union_elements:
        llist_3.append(element)
    return llist_3
    

def intersection(llist_1, llist_2):
    
    llist_1_values = llist_1.to_list_of_values()    
    llist_2_values = llist_2.to_list_of_values()   
    common_elements = set(llist_1_values)&set(llist_2_values)
    llist_3 = LinkedList()
    for element in common_elements:
        llist_3.append(element)
    return llist_3
    