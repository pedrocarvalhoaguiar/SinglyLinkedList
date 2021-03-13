from node import Node

class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, value):
        pointer = self.head
        if not pointer:
            self.head = Node(value)
        else:
            while pointer.next:
                pointer = pointer.next
            pointer = Node(value)
        self.size += 1

l = LinkedList()

l.append(1)

    
