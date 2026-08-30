class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
    
    def get(self, key):
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key, value):
        if self.cap == 0:
            return

        if key in self.cache:
            self._remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]