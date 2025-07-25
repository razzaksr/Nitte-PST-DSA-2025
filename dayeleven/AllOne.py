class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_nodes = {}
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        nxt = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = nxt
        nxt.prev = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_nodes[node.count]

    def inc(self, key):
        count = self.key_count.get(key, 0)
        new_count = count + 1
        self.key_count[key] = new_count
        curr_node = self.count_nodes.get(count)
        new_node = self.count_nodes.get(new_count)
        if not new_node:
            new_node = Node(new_count)
            self.count_nodes[new_count] = new_node
            if not curr_node: self._add_node_after(new_node, self.head)
            else: self._add_node_after(new_node, curr_node)
        new_node.keys.add(key)
        if curr_node:
            curr_node.keys.remove(key)
            if not curr_node.keys: self._remove_node(curr_node)

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        new_count = count - 1

        curr_node = self.count_nodes[count]
        curr_node.keys.remove(key)

        if new_count == 0:
            del self.key_count[key]
        else:
            self.key_count[key] = new_count
            new_node = self.count_nodes.get(new_count)
            if not new_node:
                new_node = Node(new_count)
                self.count_nodes[new_count] = new_node
                self._add_node_after(new_node, curr_node.prev)
            new_node.keys.add(key)

        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("hello")
obj.inc("hello")
print(obj.getMaxKey())
print(obj.getMinKey())
obj.inc("leet")
obj.inc("leet")
obj.inc("leet")
print(obj.getMaxKey())
print(obj.getMinKey())
    