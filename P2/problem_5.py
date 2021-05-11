## Problem-5 Autocomplete with Tries


## Get defaultdict from collections module
from collections import defaultdict

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.word_end = False
        self.children = defaultdict(TrieNode)
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char]
        
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
           
        def traverse(key,node,suffix):
            suffix += key
            if node.word_end:
                suffixes_out.append(suffix)
                    
            children = node.children
            if len(children)== 0:
                return                
            for key,node in children.items():
                traverse(key,node,suffix)
                
        suffixes_out = list()
        
        for key,node in self.children.items():
            traverse(key,node,suffix)
            
        return suffixes_out  
            
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.word_end = True
        
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root       
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node
        
## Testing it all out        
        
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    MyTrie.insert(word) 

    
## Test case-1: suffixes for the node 'f    
MyTrie.find('f').suffixes()

## Output###

"""
['un', 'unction', 'actory']

"""
## Test case-2: suffixes for the full word 'function'
MyTrie.find('function').suffixes()

## Output###

"""
[]

"""
## Test case-3: suffixes for the root node
MyTrie.find('').suffixes()

## Output###

"""

['ant',
 'anthology',
 'antagonist',
 'antonym',
 'fun',
 'function',
 'factory',
 'trie',
 'trigger',
 'trigonometry',
 'tripod']

"""


        
               