class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def printList(self, node):
        while(node is not None):
            print(node.data, end=" ")
            node = node.next
        print()

    def reverseDLL(self):
        temp = None
        curr_ptr = self.head
        if(curr_ptr is None or (curr_ptr.prev is None and curr_ptr.next is None)):
            return
        while(curr_ptr):
            temp = curr_ptr.prev
            curr_ptr.prev = curr_ptr.next
            curr_ptr.next = temp
            curr_ptr = curr_ptr.prev
        self.head = temp.prev


if __name__ == "__main__":
    dll = DLL()

    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)

    dll.printList(dll.head)
    dll.reverseDLL()
    dll.printList(dll.head)
