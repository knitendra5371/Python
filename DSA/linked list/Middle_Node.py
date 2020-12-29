class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def middle_node(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while(fast_ptr is not None and fast_ptr.next is not None):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        print("middle node data is ", slow_ptr.data)


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(50)
    llist.head.next = Node(20)
    llist.head.next.next = Node(15)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(10)

    llist.middle_node()
