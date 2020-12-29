class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def Nth_Node_FromLast(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        cnt = 1
        while(cnt < n):
            if(ref_ptr is None):
                print("n is greater than length of linked list", end="\n")
                return
            cnt += 1
            ref_ptr = ref_ptr.next
        while(ref_ptr is not None):
            ref_ptr = ref_ptr.next
            if(ref_ptr is None):
                print(n, "\bth node data from last is ", main_ptr.data)
            main_ptr = main_ptr.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(50)
    llist.head.next = Node(20)
    llist.head.next.next = Node(15)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(10)
    n = int(input("Enter Node number from last\n"))
    llist.Nth_Node_FromLast(n)
