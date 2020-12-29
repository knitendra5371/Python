class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def segregateNode(self, llist):
        Fcurr_ptr = llist
        Fprev_ptr = None
        Lcurr_ptr = llist
        while(Lcurr_ptr.next):
            Lcurr_ptr = Lcurr_ptr.next
        print(Lcurr_ptr.data)
        lastNode = Lcurr_ptr
        # print(Fcurr_ptr, " ", Lcurr_ptr)
        while(Fcurr_ptr != lastNode):
            if(Fcurr_ptr.data % 2 != 0):
                Lcurr_ptr.next = Fcurr_ptr
                Fcurr_ptr = Fcurr_ptr.next
                Lcurr_ptr = Lcurr_ptr.next
                Lcurr_ptr.next = None
                if(Fprev_ptr):
                    Fprev_ptr.next = Fcurr_ptr
                else:
                    self.head = Fcurr_ptr
            else:
                Fprev_ptr = Fcurr_ptr
                Fcurr_ptr = Fcurr_ptr.next


if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.push(6)
    llist1.push(7)
    llist1.push(1)
    llist1.push(4)
    llist1.push(5)
    llist1.push(10)
    llist1.push(12)
    llist1.push(8)
    llist1.push(15)
    llist1.push(17)
    llist1.printList()
    llist1.segregateNode(llist1.head)
    llist1.printList()
