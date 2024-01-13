class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Example Usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

print("Doubly Linked List (Forward):")
dll.display_forward()
print("hii Aashu Kumar jha")
print("\nDoubly Linked List (Backward):")
dll.display_backward()
