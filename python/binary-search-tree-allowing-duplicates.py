class Node:
    def __init__(self,item) :
        self.item=item
        self.left=None
        self.right=None
        self.count=1

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.item),f"({root.count})","->",end="")
        inorder(root.right)

def insert(node,item):
    if node==None:
        return Node(item)
    if item==node.item:
        node.count+=1
    if item<node.item:
        node.left=insert(node.left,item)
    if item>node.item:
        node.right=insert(node.right,item)    
    return node

root = None

root=insert(root,100)
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
root=insert(root,95)


root=insert(root,458)
root=insert(root,124)
root=insert(root,15)
root=insert(root,29)
root=insert(root,73)
root=insert(root,459)

root = insert(root, 12)
root = insert(root, 20)
root = insert(root, 9)
root = insert(root, 11)
root = insert(root, 10)
root = insert(root, 10)
root = insert(root, 12)
root = insert(root, 12)

inorder(root)