class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Inorder(root, al):
    if root:
        Inorder(root.left, al)
        al.append(root.data)
        Inorder(root.right, al)


def al_to_BST(root, al):
    if root:
        al_to_BST(root.left, al)
        root.data = al[0]
        al.pop(0)
        al_to_BST(root.right, al)


def BT_to_BST(root):
    al = []
    Inorder(root, al)
    al.sort()
    al_to_BST(root, al)


def print_Inorder(root):
    if root:
        print_Inorder(root.left)
        print(root.data, end=" ")
        print_Inorder(root.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    BT_to_BST(root)
    print("Inorder of BST")
    print_Inorder(root)
    print()
