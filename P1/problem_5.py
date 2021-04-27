## Problem-5 Blockchain

import hashlib,pytz
from datetime import datetime,timezone

class Block:
    
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        
    def calc_hash(self,data):
        sha = hashlib.sha256()
        sha.update(data.encode('utf-8'))
        return sha.hexdigest()
    
    def get_hash(self):
        return self.hash
    
    def get_previous_hash(self):
        return self.previous_hash
    
    def get_data(self):
        return self.data
    
    def get_timestamp(self):
        return self.timestamp
    
    
    def __str__(self):
        fmt = '%Y-%m-%d %H:%M:%S.%f %Z%z'
        s= 'Block(\n Timestamp:{}\n Data:{}\n SHA256_hash:{}\n Prev_hash:{} )'\
        .format(self.get_timestamp().strftime(fmt),self.get_data(),self.get_hash(),self.get_previous_hash())
        return s
        
    def __repr__(self):
        fmt = '%Y-%m-%d %H:%M:%S.%f %Z%z'
        s= 'Block(\n Timestamp:{}\n Data:{}\n SHA256_hash:{}\n Prev_hash:{} )'\
        .format(self.get_timestamp().strftime(fmt),self.get_data(),self.get_hash(),self.get_previous_hash())
        return s  
        
        


class BlockChain:
    
    def __init__(self):
        
        self.tail = None
        self._blocks_dict = dict()
        
    def append(self,data):        
                
        if self.tail is None:
            self.tail = Block(self.__create_timestamp(),data,0)                        
        else:
            self.tail = Block(self.__create_timestamp(),data,previous_hash=self.tail.get_hash())
            
        self._blocks_dict[self.tail.get_hash()]=self.tail
            
        
    def __iter__(self): 
        
        tail = self.tail        
        while tail.get_previous_hash() !=0:
            yield tail
            tail = self._get_block_using_hash(tail.get_previous_hash())
            
        yield tail
        
    def __create_timestamp(self):
        
        gmtz= pytz.timezone('GMT') 
        return datetime.now(tz=gmtz)
        
            
    def _get_block_using_hash(self,hash_):
        
        return self._blocks_dict[hash_]
    
    def size(self):
        return len(self._blocks_dict)
    
    def to_list(self):
        return [i for i in self][::-1]
    
    def __repr__(self):
         return '\n\n'.join([str(i) for i in self][::-1])
    