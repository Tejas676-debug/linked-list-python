class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("Linked List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if n <= 0:
                raise ValueError("Index must be a positive integer.")

            if not self.head:
                raise IndexError("Cannot delete from an empty list.")

            if n == 1:
                print(f"Deleting node at position {n} with value {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Index out of range.")

            print(f"Deleting node at position {n} with value {current.next.data}")
            current.next = current.next.next

        except (IndexError, ValueError) as e:
            print("Error:", e)


if __name__ == "__main__":
    ll = LinkedList()
    for value in [5, 15, 25, 35, 45]:
        ll.append(value)

    print("Original Linked List:")
    ll.print_list()

    ll.delete_nth_node(3)
    print("After deleting 3rd node:")
    ll.print_list()

    ll.delete_nth_node(1)
    print("After deleting 1st node:")
    ll.print_list()

    ll.delete_nth_node(10)

    empty_ll = LinkedList()
    empty_ll.delete_nth_node(1)
