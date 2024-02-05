from collections import OrderedDict

class LRUCache:
    def __init__(self,capacity: int):
        # Initialize an ordered dictionary to store key-value pairs in insertion order
        self.dic = OrderedDict()

        # Set the capacity of the LRU cache
        self.capacity = capacity
        

    def get(self,key:int) -> int:
        # Check if the key is present in the cache
        if key not in self.dic:
            # Key not present, return -1 as specified in the problem
            return -1
        else:
            # Key is present, move it to the end to mark it as recently used
            self.dic.move_to_end(key)

            # Return the corresponding value
            return self.dic[key]
    
    def put(self, key:int,value:int)-> None:
        # Check if the key is already present in the cache
        if key in self.dic:
            # Key is present, update its value and move it to the end to mark it as recently used
            self.dic[key]=value
            self.dic.move_to_end(key)
        else:
            # Key is not present, add it to the cache with the specified value
            self.dic[key]=value
            if len(self.dic)>self.capacity:
                # If the cache is full, remove the least recently used item (first item in OrderedDict)
                self.dic.popitem(last=False)
        
        return None

obj=LRUCache(2)
print(obj.put(1,1))
print(obj.put(2,2))
print(obj.get(1))
print(obj.put(3,3))
print(obj.get(2))
print(obj.put(4,4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
