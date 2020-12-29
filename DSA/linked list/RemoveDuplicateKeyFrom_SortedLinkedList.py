class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def remove_duplicates(self):
        main_ptr = self.head

        while(main_ptr is not None):
            if(main_ptr.next is None):
                return
            if(main_ptr.next.data == main_ptr.data):
                temp = main_ptr.next.next
                main_ptr.next = None
                main_ptr.next = temp
            else:
                main_ptr = main_ptr.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(20)
    llist.push(13)
    llist.push(13)
    llist.push(11)
    llist.push(11)
    llist.push(11)

    llist.printList()
    llist.remove_duplicates()
    llist.printList()
