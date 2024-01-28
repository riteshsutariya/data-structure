class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

# insertion
def insert(node,item):
    if node==None:
        return Node(item)
    if item<node.item:
        node.left=insert(node.left,item)
    if item>node.item:
        node.right=insert(node.right,item)
    return node

def findMinNode(root):
    if root==None:
        return root
    else:
        while(root.left!=None):
            root=root.left
    return root

def findMaxNode(root):
    if root is None:
        return root
    while root.right is not None:
        root=root.right
    return root

def deleteNode(root,item):
    if root is None:
        return root
    # traverse to target node
    if item<root.item:
        root.left=deleteNode(root.left,item)
    elif item>root.item:
        root.right=deleteNode(root.right,item)
    else:
        if root.left is None:
            temp=root.right
            del root
            return temp
        elif root.right is None:
            temp=root.left
            del root
            return temp
        else:
            temp=findMaxNode(root.left)
            root.item=temp.item
            root.left=deleteNode(root.left,temp.item)
            # OR
            # temp=findMinNode(root.right)
            # root.item=temp.item
            # root.right=deleteNode(root.right,temp.item)
            
    return root

count=0

def search(root,item):
    global count
    count+=1
    if root is None or root.item==item:
        return root
    if item<root.item:
        return search(root.left,item)
    else:
        return search(root.right,item)

# traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.item),"->",end="")
        inorder(root.right)

def preorder(root):
    if root:
        print(str(root.item),"->",end="")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.item),"->",end="")

root=None
root=insert(root,100)
root=insert(root,30)
root=insert(root,70)
root=insert(root,20)
root=insert(root,40)
root=insert(root,60)
root=insert(root,80)

root=insert(root,10)
root=insert(root,25)
root=insert(root,35)
root=insert(root,45)
root=insert(root,50)
root=insert(root,12)
root=insert(root,45)
root=insert(root,178)
root=insert(root,98)
root=insert(root,116)
root=insert(root,5)

root=insert(root,45)
root=insert(root,95)
root=insert(root,167)
root=insert(root,84)
root=insert(root,120)
root=insert(root,195)

root=insert(root,110)
root=insert(root,190)
root=insert(root,450)

root=insert(root,458)
root=insert(root,124)
root=insert(root,15)
root=insert(root,29)
root=insert(root,73)
root=insert(root,459)

print("\nINORDER:-")
inorder(root)

# root=deleteNode(root,50)

# print("\nafter removing 20,INORDER:-")
# inorder(root)

# print("\nPRE ORDER:-")
# preorder(root)

# print("\nPOST ORDER")
# postorder(root)

# print("\n\n\nMin Node:")
# print(findMinNode(root).item)

print("Search: ")
item=int(input("Enter value to search:"))

result=search(root,item)
if result is not None:
    print("item found")
else:
    print("not found!")

print(f"total {count} iteration for search")