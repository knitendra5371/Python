class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(r, data):
    # print("i m inside insert function ", r)
    if(r == None):
        r = Node(data)
        # print("i m inside insert function ", r, r.data)
    elif(r.data > data):
        if(r.left == None):
            r.left = Node(data)
        else:
            insert(r.left, data)
    elif(r.data < data):
        if(r.right == None):
            r.right = Node(data)
        else:
            insert(r.right, data)


'''
5 2 7 1 6 3 8
10 5 3 15 13 18 8 9 6 7 2 1 4 16 17 12 14
5 8 4 7 6
15 9 16 6 11 5 8 7 10 13 12 14
'''

#################################### Inorder of BST ##########################


def inorder(r):
    # print("inside inorder", r)
    if(r):
        # print("***")
        inorder(r.left)
        print(r.data, end=" ")
        inorder(r.right)


################################### Preorder of BST #############################

def preorder(r):
    if(r):
        print(r.data, end=" ")
        preorder(r.left)
        preorder(r.right)


################################### Postorder of BST #################################

def postorder(r):
    if(r):
        postorder(r.left)
        postorder(r.right)
        print(r.data, end=" ")


##################################### Height of BST ###################################

def height(r):
    if(r == None):
        return 0
    return 1+max(height(r.left), height(r.right))

############################################################################################


a = input("Enter data for  BST\n").split()
r = Node(int(a[0]))
# print(r)
del a[0]
for i in a:
    insert(r, int(i))
    # print("value of r inside for loop ", r)
print("Inorder of BST => ", end=" ")
inorder(r)
print("\nPreorder of BST => ", end=" ")
preorder(r)
print("\nPostorder of BST => ", end=" ")
postorder(r)
print("\nheight of BST => ", height(r), end=" ")
print()


############################################ Lavel by BST ###############################

labelByBST = []
labelByBST.append(r)
print("label By BST => ", end=" ")
for item in labelByBST:
    print(item.data, end=" ")
    if(item.left):
        labelByBST.append(item.left)
    if(item.right):
        labelByBST.append(item.right)

labelByBST.clear()

############################## Leaf Node's of BST ###########################


def leafNode(r):
    if(r == None):
        return
    if(r.left == None and r.right == None):
        print(r.data, end=" ")
    leafNode(r.left)
    leafNode(r.right)


print("\nLeaf Nodes of BST => ", end=" ")
leafNode(r)
print()
# print(labelByBST)


################################### Zig zag print BST #########################


def ZigZagBST(r):
    a = []
    b = []
    if(r == None):
        return
    a.append(r)
    while(len(a) > 0 or len(b) > 0):
        while(len(a) > 0):
            item1 = a.pop()
            print(item1.data, end=" ")
            if(item1.left):
                b.append(item1.left)
            if(item1.right):
                b.append(item1.right)
        while(len(b) > 0):
            item2 = b.pop()
            print(item2.data, end=" ")
            if(item2.right):
                a.append(item2.right)
            if(item2.left):
                a.append(item2.left)


print("Zig Zag BST => ", end=" ")
ZigZagBST(r)
print()

#################################### Mirror Image of BST ###########################


def swap(a, b):
    return b, a


def Mirror_image_BST(r):
    if(r == None):
        return
    r.left, r.right = swap(r.left, r.right)
    Mirror_image_BST(r.left)
    Mirror_image_BST(r.right)


Mirror_image_BST(r)
print("label by Mirror Image of BST => ", end=" ")
labelByBST = []
labelByBST.append(r)

for item in labelByBST:
    print(item.data, end=" ")
    if(item.left):
        labelByBST.append(item.left)
    if(item.right):
        labelByBST.append(item.right)

# labelByBST.clear()
print()
Mirror_image_BST(r)
######################################## Left view of BST ##########################


def Left_View_BST(root, level, max_level):
    if root is None:
        return
    if(max_level[0] < level):
        print(root.data, end=" ")
        max_level[0] = level
    # print(max_level)
    # print(id(v), " ", id(h))
    Left_View_BST(root.left, level+1, max_level)
    Left_View_BST(root.right, level+1, max_level)


# print(id(v))
max_level = [0]
print("Left view of BST => ", end=" ")
Left_View_BST(r, 1, max_level)

print()

############################################### Right view of BST ###########################


def Right_view_BST(root, level, max_level):
    if(root is None):
        return
    if(max_level[0] < level):
        print(root.data, end=" ")
        max_level[0] = level
    Right_view_BST(root.right, level+1, max_level)
    Right_view_BST(root.left, level+1, max_level)


max_level[0] = 0
print("Right view of BST => ", end=" ")
Right_view_BST(r, 1, max_level)
print()

######################################### Boundry elements of BST ############################


def left_elements(rl):
    if(rl):
        if(rl.left):
            print(rl.data, end=" ")
            left_elements(rl.left)
        elif(rl.right):
            print(rl.data, end=" ")
            left_elements(rl.right)


def right_elements(rr):
    if(rr):
        if(rr.right):
            print(rr.data, end=" ")
            right_elements(rr.right)
        elif(rr.left):
            print(rr.data, end=" ")
            right_elements(rr.left)


def Boundry_elements(root):
    left_elements(root)
    leafNode(root)
    right_elements(root.right)


print("Boundry elements of BST => ", end=" ")
Boundry_elements(r)
print()


########################################## Diameter of BST #############################

diameter = [0]
center_node = [-1]


def diameter_BST(root):
    if(root):
        if(diameter[0] < height(root.left)+1+height(root.right)):
            diameter[0] = height(root.left)+1+height(root.right)
            center_node[0] = root.data
        diameter_BST(root.left)
        diameter_BST(root.right)


diameter_BST(r)
print("Diameter of BST => ", diameter[0], " ", center_node[0], end=" ")
print()


####################################### Delete a node from BST ###########################
