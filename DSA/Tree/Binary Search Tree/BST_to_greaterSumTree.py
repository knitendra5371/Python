
sum = 0


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def greaterSum(root):
    global sum
    if not root:
        return

    greaterSum(root.right)
    sum = sum + root.data
    root.data = sum-root.data
    greaterSum(root.left)


def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)


if __name__ == "__main__":
    root = Node(11)
    root.left = Node(2)
    root.right = Node(29)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(40)
    root.right.right.left = Node(35)
    print("Inorder of BST before transform\n")
    Inorder(root)
    print("\n\nInorder of BST after transform\n")
    greaterSum(root)
    Inorder(root)
    print()
