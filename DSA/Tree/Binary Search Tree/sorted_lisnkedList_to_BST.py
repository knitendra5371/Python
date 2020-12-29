head = None


class LNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LinkedList_to_BST(head, size):

    if size <= 0:
        return None
    left = LinkedList_to_BST(globals()['head'], int(size/2))
    r = TNode(globals()['head'].data)
    r.left = left
    globals()['head'] = globals()['head'].next
    r.right = LinkedList_to_BST(globals()['head'], size-int(size/2)-1)
    return r


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)


if __name__ == "__main__":

    al = input().split()
    if len(al) > 0:
        head = temp = LNode(int(al[0]))
    for i in range(1, len(al)):
        temp.next = LNode(int(al[i]))
        temp = temp.next

    r = None
    #ar = [head]
    root = LinkedList_to_BST(head, len(al))
    preorder(root)
    print()
    Inorder(root)
    print()
