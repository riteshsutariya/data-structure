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

def delete_deepest(root, target_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp == target_node:
            temp = None
            del temp
            return
        
        if temp.left:
            if temp.left == target_node:
                temp.left = None
                del target_node
                return
            else:
                q.append(temp.left)
        
        if temp.right:
            if temp.right == target_node:
                temp.right = None
                del target_node
                return
            else:
                q.append(temp.right)
        
def delete(root, value):
    if root is None:
        return None
    
    if root.left is None and root.right is None:
        if root.item == value:
            return None
        else:
            return root
    
    q = deque()
    q.append(root)
    
    temp = None
    target_node = None

    while q:
        temp = q.popleft()
        if temp.item == value:
            target_node = temp
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)

    if target_node is not None:
        target_node.item = temp.item
        delete_deepest(root, temp)
        print('targer found')
    else:
        print('target not found!')
    return root
root = None

# values = [25,50,75,15,20,29,35,45,95,28,82,92,88,91,97]
values = [25,50,75]

for value in values:
    root = insert(root,value)

print("Inorder traversal ")
inorder(root)
print()

root = delete(root,75)

print("Inorder traversal ")
inorder(root)
print()

# print("\nPreorder traversal ")
# preorder(root)

# print("\nPostorder traversal ")
# postorder(root)

# print()

