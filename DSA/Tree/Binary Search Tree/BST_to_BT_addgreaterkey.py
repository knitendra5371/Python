
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def addGreater(root, sum):
    if not root:
        return
    addGreater(root.right, sum)
    sum[0] += root.data
    root.data = sum[0]
    addGreater(root.left, sum)


def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)


if __name__ == "__main__":
    Sum = [0]
    root = Node(5)
    root.left = Node(2)
    root.right = Node(13)
    Inorder(root)
    print()
    addGreater(root, Sum)
    Inorder(root)
    print()
