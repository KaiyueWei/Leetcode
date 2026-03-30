class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: node
        self.left = Node(0, 0) # dummy head
        self.right = Node(0, 0) # dummy tail
        #self.left.next LRU, self.right.prev MRU
        self.left.next = self.right
        self.right.prev = self.left
    
    ## remove from the list
    def remove(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev
    ## insert to the right, mru
    def insert(self, node):
        old = self.right.prev
        old.next = node
        node.prev = old
        self.right.prev = node 
        node.next = self.right     

    def get(self, key: int) -> int:
        if key in self.cache:
            ## update the most recent used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #update the node
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return 
        #create a node and insert to the mru
        newNode = Node(key, value)
        if len(self.cache) == self.capacity:
            #remove lru
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)
        self.cache[key] = newNode
        self.insert(newNode)

        
