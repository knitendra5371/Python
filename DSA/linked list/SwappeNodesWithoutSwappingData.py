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

    def swapNodes(self, x, y):
        prev_ptr1 = None
        prev_ptr2 = None
        curr_ptr1 = self.head
        curr_ptr2 = self.head

        while(curr_ptr1 is not None):
            if(curr_ptr1.data == x):
                break
            prev_ptr1 = curr_ptr1
            curr_ptr1 = curr_ptr1.next

        while(curr_ptr2 is not None):
            if(curr_ptr2.data == y):
                break
            prev_ptr2 = curr_ptr2
            curr_ptr2 = curr_ptr2.next

        print(curr_ptr1.data, " ", curr_ptr2.data,
              " ", prev_ptr1, " ", prev_ptr2)
        if(curr_ptr1 is None or curr_ptr2 is None):
            print("x or y not present in linked list", end="\n")
            return
        # if(curr_ptr1 is not None and curr_ptr2 is not None):
        if(prev_ptr1 is not None):
            prev_ptr1.next = curr_ptr2
        else:
            self.head = curr_ptr2
        if(prev_ptr2 is not None):
            prev_ptr2.next = curr_ptr1
        else:
            self.head = curr_ptr1
        temp = curr_ptr1.next
        curr_ptr1.next = curr_ptr2.next
        curr_ptr2.next = temp
        # self.printList()


if __name__ == "__main__":
    llist = LinkedList()

    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.printList()

    llist.swapNodes(7, 6)
    llist.printList()
