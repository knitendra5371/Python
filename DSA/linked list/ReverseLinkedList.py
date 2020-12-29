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

    def ReverseLL(self, llist):
        prev_ptr = None
        curr_ptr = llist
        if(curr_ptr):
            next_ptr = curr_ptr.next

        while(curr_ptr):
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_ptr
            if(curr_ptr):
                next_ptr = curr_ptr.next

        self.head = prev_ptr


if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.push(30)
    llist1.push(15)
    llist1.push(9)
    llist1.push(6)
    llist1.push(3)
    llist1.printList()
    llist1.ReverseLL(llist1.head)
    print("Reverse LinkedList  ", end=" ")
    llist1.printList()
