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

    def insertInit(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

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

    def insertMid(self, index, value):
        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

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

    def removeBV(self, value):
        if not self.head:
            raise ValueError('List is empty')
        elif self.head.data == value:
            self.head = self.head.next
            self.__size -= 1
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == value:
                    ancestor.next = pointer.next
                    self.__size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next
            raise ValueError(f'{value} is not in list')

    def index(self, value):
        pointer = self.head
        count = 0
        while pointer:
            if pointer.data == value:
                return count
            else:
                pointer = pointer.next
                count += 1
        raise ValueError(f'{value} is not in list')

    def removeBI(self, index):
        if index < 0:
            raise ValueError("Can't interate with negative value")
        elif self.head == None:
            raise ValueError('list is empity')
        elif self.head == self._getNode(index):
            self.head = self.head.next
            self.__size -= 1
            return True
        elif self.head.next == None:
            self.head = self.head.next
            self.__size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer != self._getNode(index):
                ancestor = pointer
                pointer = pointer.next
            try:
                ancestor.next = pointer.next
                self.__size -= 1
                return True
            except:
                raise IndexError('index out of range')

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + " -> "
            pointer = pointer.next
        return '[' + r + ']'


l = LinkedList()

l.append(1)
l.append(2)
l.append(3)
l[2] = 4
print(l)
l.insert(3)
print(l)
