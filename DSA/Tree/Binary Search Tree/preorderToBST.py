
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getIndex():
    return constuctBST_Util.preIndex


def increaseIndex():
    constuctBST_Util.preIndex += 1


def constuctBST_Util(al, low, high, size):
    if getIndex() >= size or low > high:
        return None
    temp = Node(al[getIndex()])
    increaseIndex()
    if low == high:
        return temp

    for i in range(low, high+1):
        if al[i] > temp.data:
            break

    temp.left = constuctBST_Util(al, getIndex(), i-1, size)
    temp.right = constuctBST_Util(al, i, high, size)

    return temp


def constructBST(al, size):
    constuctBST_Util.preIndex = 0
    return constuctBST_Util(al, 0, size-1, size)


def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)


if __name__ == '__main__':
    # input 10 5 1 7 40 50
    al = input("Enter preorder of a BST\n").split()
    for i in range(0, len(al)):
        al[i] = int(al[i])

    root = constructBST(al, len(al))
    InOrder(root)
    print()
