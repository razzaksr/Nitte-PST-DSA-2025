class Node:
    def __init__(self, key, value):
        self.key, self.val, self.prev, self.next = key, value, None, None
    def __str__(self): 
        return "the key is "+str(self.key)+" value is "+str(self.val)
class LRUCache:
    def __init__(self, capacity):
        self.cap, self.cache, self.head = capacity, {}, Node(0, 0)
        self.tail = Node(0, 0)  # dummy tail
        self.head.next, self.tail.prev = self.tail, self.head
    def _remove(self, node):
        # Remove node from list
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def _add_to_front(self, node):
        # Add node right after head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.val
        return -1
    def put(self, key, value):
        if key in self.cache: self._remove(self.cache[key])
        node = Node(key, value)
        self._add_to_front(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            # Remove LRU node
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
lRUCache = LRUCache(2)
lRUCache.put(1, 10)
lRUCache.put(2, 100)
print(lRUCache.get(1))  # 1
lRUCache.put(3, 1000)
print(lRUCache.get(2))  # -1
lRUCache.put(4, 10000)
print(lRUCache.get(1))  # -1
print(lRUCache.get(3))  # 3
print(lRUCache.get(4))  # 4