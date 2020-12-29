
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def Inorder(root, al):
    if root:
        Inorder(root.left, al)
        al.append(root.data)
        Inorder(root.right, al)


def BST_to_minHeap(root, al):
    if root:
        root.data = al[0]
        al.pop(0)
        BST_to_minHeap(root.left, al)
        BST_to_minHeap(root.right, al)


def PreOrder(root):
    if root:
        print(root.data, end=" ")
        PreOrder(root.left)
        PreOrder(root.right)


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    al = []
    Inorder(root, al)
    BST_to_minHeap(root, al)
    PreOrder(root)
    print()
