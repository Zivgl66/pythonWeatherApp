class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def pop(self):
        if self.head is None:
            return

        current_node = self.head
        if current_node.next is not None:
            while current_node.next.next:
                current_node = current_node.next
            data = current_node.next.data
            current_node.next = None
        else:
            data = current_node.data
            self.head = None

        return data

    def get_head(self):
        return self.head.data

    def get_len(self):
        counter = 0
        if self.head is None:
            return counter
        counter += 1
        current_node = self.head
        while current_node.next:
            counter += 1
            current_node = current_node.next
        return counter

    def is_empty(self):
        return self.head is None



linked_list = LinkedList()
print(linked_list.is_empty())
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
print(linked_list.get_len())
print(linked_list.pop())
print(linked_list.get_head())
print(linked_list.get_len())
print(linked_list.is_empty())
