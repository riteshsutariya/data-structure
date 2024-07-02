class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, value):
    if root is None:
        return Node(value)
    
    if root.value > value:
        root.left = insert(root.left,value)
    elif root.value < value:
        root.right = insert(root.right,value)
    return root

def search(root,target):
    if root is None:
        return None
    if root.value == target:
        return root
    if root.value > target:
        return search(root.left, target)
    elif root.value < target:
        return search(root.right, target)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value,end='->')
        inorder(root.right)
        
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end='->')
        
def preorder(root):
    if root is not None:
        print(root.value,end='->')
        preorder(root.left)
        preorder(root.right)
    
def findMinNode(root):
    if root is None:
        return None
    else:
        while root.left is not None:
            root = root.left
    return root

def deletion(root,target):
    if root is None:
        return None
    if root.value < target:
        root.right = deletion(root.right,target)
    elif root.value > target:
        root.left = deletion(root.left,target)
    else:
        if root.left is None:
            temp = root.right
            del root.right
            return temp
        elif root.right is None:
            temp = root.left
            del root.left
            return temp
        else:
            temp = findMinNode(root.right)
            root.value = temp.value
            deletion(root.left, temp.item)
    return root 


root = insert(None,48)
root = insert(root,20)
root = insert(root,3)
root = insert(root,5)
root = insert(root,7)
root = insert(root,14)
root = insert(root,25)
root = insert(root,22)
root = insert(root,30)

root = insert(root,45)
root = insert(root,51)
root = insert(root,26)
root = insert(root,65)
root = insert(root,95)
root = insert(root,15)
root = insert(root,84)
root = insert(root,56)
root = insert(root,77)
root = insert(root,92)

inorder(root)
print()

deletion(root,77)

inorder(root)
print()
# preorder(root)
# print()
# postorder(root)
# print()
# result = search(root,95)
# if result is None:
#     print('target miss')
# else:
#     print('target hit')