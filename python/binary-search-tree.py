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

# deletion
def delete(root,item):
    # base condition
    if root is None:
        return root
    
    # recursive calls for ancestors of 
    # node to be deleted
    if root.item>item:
        root.left=delete(root.left,item)
        return root
    elif root.item<item:
        root.right=delete(root.right,item)

    # here root is the node to be deleted
    
    # if one of the children is empty
    if root.left is None:
        temp=root.right
        del root
        return temp
    if root.right is None:
        temp=root.left
        del root
        return temp
 
    #if both children exists
    succParent=root
     
    # find successor
    succ=root.right
    while succ.left is not None:
        succParent=succ
        succ=succ.left

    if succParent!=root:
        succParent.left=succ.right
    else:
        succParent.right=succ.right

    # delete successor and return root
    del succ
    return root

def search(root,item):
    if root==None or root.item==item:
        return root

    if root.item<item:
        return search(root.right,item)

    return search(root.left,item)

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
root=insert(root,50)
root=insert(root,30)
root=insert(root,70)
root=insert(root,20)
root=insert(root,40)
root=insert(root,60)
root=insert(root,80)
# root=Node(100)
# root=insert(root,12)
# root=insert(root,45)
# root=insert(root,178)
# root=insert(root,98)
# root=insert(root,116)
# root=insert(root,5)

# root=insert(root,45)
# root=insert(root,95)
# root=insert(root,167)
# root=insert(root,84)
# root=insert(root,120)
# root=insert(root,95)


# root=insert(root,458)
# root=insert(root,124)
# root=insert(root,15)
# root=insert(root,29)
# root=insert(root,73)
# root=insert(root,459)

print("\nINORDER:-")
inorder(root)

root=delete(root,20)

print("\nafter removing 20,INORDER:-")
inorder(root)

print("\nPRE ORDER:-")
preorder(root)

print("\nPOST ORDER")
postorder(root)

# print("\n\n\nMin Node:")
# print(findMinNode(root).item)

print("Search: ")
item=int(input("Enter value to search:"))

result=search(root,item)
if result is not None:
    print("item found")
else:
    print("not found!")