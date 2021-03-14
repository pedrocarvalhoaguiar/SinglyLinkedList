from node import Node

# create list class


class LinkedList():

    def __init__(self):
        self.head = None
        self.__size = 0

    def append(self, value):
        pointer = self.head
        if not pointer:
            self.head = Node(value)
        else:
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(value)
        self.__size += 1

    def __len__(self):
        return self.__size

    def _getNode(self, index):
        pointer = self.head
        for n in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('List index out of range')
        return pointer

    def __getitem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError('List index out of range')

    def __setitem__(self, index, value):
        pointer = self._getNode(index)
        if pointer:
            pointer.data = value
        else:
            raise IndexError('List index out of range')

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + " -> "
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()



l = LinkedList()

l.append(4)
l.append(5)

print(l[2])
