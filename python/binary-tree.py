from collections import deque

class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

def inorder(root):
    if root:
        # traverse left
        inorder(root.left)
        # traverse root
        print(str(root.item)+'->',end='')
        # traverse right
        inorder(root.right)

def postorder(root):
    if root:
        # traverse left
        postorder(root.left)
        # traverse right
        postorder(root.right)
        # traverse root
        print(str(root.item)+'->',end='')

def preorder(root):
    if root:
        # traverse root
        print(str(root.item)+'->',end='')
        # traverse left
        preorder(root.left)
        # traverse right
        preorder(root.right)
        
def insert(root, value):
    # if tree is empty, new node will be root node 
    if root is None:
        root = Node(value)
        return root
    
    # using queue to find node for insertion
    q = deque()
    q.append(root)
    
    while q:
        temp = q.popleft()
        print('temp:- ',temp.item)
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

def delete(root, value):
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        if root.value == value:
            return None
        else:
            return root
        

root = None

values = [25,50,75,15,20,29,35,45,95,28,82,92,88,91,97]

for value in values:
    root = insert(root,value)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)

print()