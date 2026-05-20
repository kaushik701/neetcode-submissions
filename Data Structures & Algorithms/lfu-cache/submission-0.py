from collections import defaultdict

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Dummy head and tail to simplify operations
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self) -> bool:
        return self.head.next == self.tail

    def add_first(self, node: Node) -> None:
        # Insert right after head (MRU position for this frequency)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node) -> None:
        # Remove a specific node
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None

    def remove_last(self) -> Node:
        # Remove LRU node for this frequency (just before tail)
        if self.is_empty():
            return None
        node = self.tail.prev
        self.remove(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.nodeMap = {}                   # key -> Node
        self.freqMap = defaultdict(DoublyLinkedList)  # freq -> DoublyLinkedList

    def _update_freq(self, node: Node) -> None:
        # Remove from old freq list
        old_freq = node.freq
        old_list = self.freqMap[old_freq]
        old_list.remove(node)

        # If this list becomes empty and was the minFreq, bump minFreq
        if old_list.is_empty() and old_freq == self.minFreq:
            self.minFreq += 1

        # Increase node frequency and add to new list
        node.freq += 1
        new_list = self.freqMap[node.freq]
        new_list.add_first(node)

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodeMap:
            # Update value and bump frequency
            node = self.nodeMap[key]
            node.value = value
            self._update_freq(node)
            return

        # Evict if at capacity
        if self.size == self.capacity:
            # Least frequently used nodes are in freqMap[minFreq]
            lfu_list = self.freqMap[self.minFreq]
            node_to_remove = lfu_list.remove_last()  # LRU within that freq
            if node_to_remove:
                del self.nodeMap[node_to_remove.key]
                self.size -= 1

        # Insert new node with freq 1
        new_node = Node(key, value)
        self.nodeMap[key] = new_node
        self.freqMap[1].add_first(new_node)
        self.minFreq = 1
        self.size += 1