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
        st = set([])
        curr_ptr = self.head
        prev_ptr = None
        while(curr_ptr is not None):
            if(curr_ptr.data not in st):
                st.add(curr_ptr.data)
                prev_ptr = curr_ptr
                curr_ptr = curr_ptr.next
            else:
                prev_ptr.next = curr_ptr.next
                curr_ptr = None
                curr_ptr = prev_ptr.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(21)
    llist.push(43)
    llist.push(41)
    llist.push(21)
    llist.push(12)
    llist.push(11)
    llist.push(12)

    llist.printList()
    llist.remove_duplicates()
    llist.printList()
