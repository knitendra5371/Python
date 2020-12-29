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

    def swapElements(self):
        temp1 = None
        temp2 = None
        if(self.head is not None):
            temp1 = self.head
            if(self.head.next is not None):
                temp2 = self.head.next

        while(temp1 and temp2):
            d = temp1.data
            temp1.data = temp2.data
            temp2.data = d
            temp1 = temp2.next
            # temp2 = temp1 != None ? temp1.next: None
            if(temp1):
                temp2 = temp1.next
            else:
                temp2 = None


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)

    llist.printList()
    llist.swapElements()
    llist.printList()

    llist.push(1)
    print("\n\n")
    llist.printList()
    llist.swapElements()
    llist.printList()
