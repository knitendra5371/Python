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

    def IntersectionPoint(self, llist1, llist2):
        cnt1, cnt2 = 0, 0
        temp = llist1
        while(temp):
            cnt1 += 1
            temp = temp.next

        temp = llist2
        while(temp):
            cnt2 += 1
            temp = temp.next
        # print(cnt1, " ", cnt2)
        temp1 = llist1
        temp2 = llist2
        if(cnt1 > cnt2):
            l = cnt1-cnt2+1
            while(l > 1):
                temp1 = temp1.next
                l -= 1
        if(cnt2 > cnt1):
            l = cnt2-cnt1+1
            while(l > 1):
                temp2 = temp2.next
                l -= 1
        while(temp1 and temp2):
            if(temp1.data == temp2.data):
                print("1st method , Intersection Point is = ", temp1.data)
                break
            temp1 = temp1.next
            temp2 = temp2.next

    def IntersectionPointBySet(self, llist1, llist2):
        st = set([])
        temp = llist1
        while(temp):
            st.add(temp)
            temp = temp.next
        temp = llist2
        while(temp):
            if(temp in st):
                print("2nd method , Intersection Point is = ", temp.data)
                break
            temp = temp.next


if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.push(30)
    llist1.push(15)
    llist1.push(9)
    llist1.push(6)
    llist1.push(3)

    llist2 = LinkedList()
    # llist2.push(30)
    # llist2.push(15)
    llist2.push(10)
    llist2.head.next = llist1.head.next.next.next
    llist1.printList()
    llist2.printList()

    llist1.IntersectionPoint(llist1.head, llist2.head)
    llist1.IntersectionPointBySet(llist1.head, llist2.head)
