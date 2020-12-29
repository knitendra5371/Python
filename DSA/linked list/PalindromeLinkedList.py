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

    def reverseList(self, l):
        print(l.data)
        prev_ptr = None
        curr_ptr = l
        if(curr_ptr):
            next_ptr = curr_ptr.next

        while(curr_ptr):
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_ptr
            if(curr_ptr):
                next_ptr = curr_ptr.next

        return prev_ptr

    def checkPalindrome(self, list):
        # print(list)
        slow_ptr = list
        fast_ptr = list
        fh_ptr = None
        while(fast_ptr and fast_ptr.next):
            fh_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if(fast_ptr):
            fh_ptr = fh_ptr.next
            fh_ptr.next = self.reverseList(slow_ptr.next)
        else:
            fh_ptr.next = self.reverseList(slow_ptr)
        self.printList()
        temp1 = self.head
        temp2 = fh_ptr.next
        while(temp2):
            if(temp1.data != temp2.data):
                print("Linked List is not a Palindrome ")
                break
            temp1 = temp1.next
            temp2 = temp2.next
        if(temp2 is None):
            print("Linked List is a Palindrome")


if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.push(1)
    llist1.push(2)
    llist1.push(3)
    llist1.push(4)
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)
    llist1.printList()
    llist1.checkPalindrome(llist1.head)
