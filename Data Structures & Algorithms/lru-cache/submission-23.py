class Node:
    def __init__(self, val, key):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def get(self, key):
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, val):
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(val, key)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
        

        