class LinkedList:
    # defining structure of the node
    class Node:
        def __init__(self, value):
            self.value = value  # value/data of the node
            self.next = None    # reference to the next node

    def __init__(self):
        self.head = None  # initializing head of the linked list

    # 1st method:
    def insert_at_end(self, value):
        new_node = self.Node(value)

        if self.head == None:
            self.head = new_node
            return


        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 2nd method:
    def insert_at_start(self, value):
        new_node = self.Node(value)
        new_node.next = self.head
        self.head = new_node

    # 3rd method:
    def insert_at_index(self, index, value):
        # showing error if index given is negative
        if index < 0:
            raise IndexError("Index given is a negative index")

        # insert at the start if index is 0
        if index == 0:
            self.insert_at_start(value)
            return

        new_node = self.Node(value)
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if not current:
            raise IndexError("Invalid index")
        new_node.next = current.next
        current.next = new_node

    # 4th method:
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    # 5th method:
    def display(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print(",".join(values) if values else "empty list")

    #6th method]
    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index given is a negative index")
        if not self.head:
            raise IndexError("list is empty")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current.next and count < index - 1:
            current = current.next
            count += 1
        if not current.next:
            raise IndexError("Invalid index")
        current.next = current.next.next



# instantiation
linklistobj = LinkedList()
linklistobj.insert_at_start(18)
linklistobj.insert_at_end(500)
linklistobj.insert_at_index(1, 9)
linklistobj.delete_at_index(1)
linklistobj.display()
