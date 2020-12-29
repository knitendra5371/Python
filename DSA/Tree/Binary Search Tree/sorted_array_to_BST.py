

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Array_to_BST(al):
    if not al:
        return None
    mid = int(len(al)/2)
    r = Node(al[mid])
    r.left = Array_to_BST(al[:mid])
    r.right = Array_to_BST(al[mid+1:])
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
    for i in range(0, len(al)):
        al[i] = int(al[i])
    root = Array_to_BST(al)
    preorder(root)
    print()
    Inorder(root)
    print()
