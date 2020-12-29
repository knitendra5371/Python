class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # def push(self, data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def detect_and_removeLoop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        loop_flag = 0
        while(fast_ptr is not None and fast_ptr.next is not None):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if(slow_ptr == fast_ptr):
                loop_flag = 1
                print("loop present")
                break

        cnt_no = 1
        temp = slow_ptr.next
        while(temp != slow_ptr):
            cnt_no += 1
            temp = temp.next
        print("count nodes ", cnt_no)
        slow_ptr = self.head
        fast_ptr = self.head
        while(cnt_no > 1):
            cnt_no -= 1
            fast_ptr = fast_ptr.next
        print("cnt_no-1 node data", fast_ptr.data)
        while(slow_ptr != fast_ptr):
            if(slow_ptr == fast_ptr.next):
                fast_ptr.next = None
                break
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(50)
    llist.head.next = Node(20)
    llist.head.next.next = Node(15)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(10)
    llist.head.next.next.next.next.next = llist.head.next.next

    llist.detect_and_removeLoop()
    llist.printList()
