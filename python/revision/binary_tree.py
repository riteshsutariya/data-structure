
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value, end= ',')
        inorder(root.right)
    else:
        # print('not a valid tree')
        return None
    
def preorder(root):
    if root is not None:
        print(root.value, end=',')
        preorder(root.left)
        preorder(root.right)
    else:
        # print('not a valid tree')
        return None
    
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=',')
    else:
        # print('not a valid tree')
        return None
    
def insert(root, value):
    # tree not having any node
    if root is None:
        return Node(value)
    
    # tree with root only
    if root.left is None and root.right is None:
        root.left = Node(value)
        return root
    
    q = deque()
    q.append(root)
    
    while q:
        temp = q.popleft()
        if temp.left is None:
            temp.left = Node(value)
            break
        else:
            q.append(temp.left)
        
        if temp.right is None:
            temp.right = Node(value)
            break
        else:
            q.append(temp.right)
        
    return root

# root = Node(10)
# root.left = Node(12)
# root.left.left = Node(20)
# root.left.right = Node(24)
# root.left.left.left = Node(38)
# root.left.left.right = Node(40)

# root.right = Node(18)
# root.right.left = Node(28)
# root.right.right = Node(32)
# root.right.left.left = Node(45)
# root.right.right.right = Node(50)

root = None

nodes = [2,4,6,12,18,24,38,54,38,40,90,45,94,99,120]

for node in nodes:
    root = insert(root,node)

print('in order:')
inorder(root)
print()
print('pre order:')
preorder(root)
print()
print('post order')
postorder(root)
print()