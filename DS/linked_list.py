class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        index = 0
        current = self.head
        result = 'Linked List[ '
        while current != None:
            index += 1
            if index == 1:  # node dau tien
                result += ' ' + str(current.value)
            else:  # tu node thu 2 tro di
                result += ' -> ' + str(current.value)
            current = current.next  # cap nhat current
        result += ' ]'
        print(result)

    def add(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert(self, index, value):
        node = Node(value)
        previous = None
        current = self.head
        i = 0
        while i < index and current != None:
            i += 1
            previous = current
            current = current.next
        #
        if previous == None:
            # them vao dau ds
            node.next = self.head

    def search(self, value):
        pass

    def remove(self, value):
        pass

    def clear(self):
        pass
