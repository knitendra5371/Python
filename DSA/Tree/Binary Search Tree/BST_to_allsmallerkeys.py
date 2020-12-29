
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)


def addSmaller(root, sum):
    if not root:
        return
    addSmaller(root.left, sum)
    sum[0] += root.data
    root.data = sum[0]
    addSmaller(root.right, sum)


if __name__ == "__main__":
    root = Node(9)
    root.left = Node(6)
    root.right = Node(15)
    Inorder(root)
    Sum = [0]
    print()
    addSmaller(root, Sum)
    Inorder(root)
    print()
