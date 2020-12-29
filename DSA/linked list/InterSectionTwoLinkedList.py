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

    def InterSection(self, llist1, llist2):
        st = set([])
        temp = llist1
        while(temp is not None):
            st.add(temp.data)
            temp = temp.next

        temp = llist2
        while(temp is not None):
            if(temp.data in st):
                print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.push(6)
    llist1.push(4)
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)

    llist2 = LinkedList()
    llist2.push(8)
    llist2.push(6)
    llist2.push(4)
    llist2.push(2)

    llist1.printList()
    llist2.printList()
    llist1.InterSection(llist1.head, llist2.head)
