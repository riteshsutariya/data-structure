class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

def inorder(root):
    if root:
        #process left
        inorder(root.left)
        #process root
        print(str(root.item),'->',end='')
        #process right
        inorder(root.right)

def insert(node,item):
    if node is None:
        return Node(item)
    # traverse to the right place and insert the node
    if item<node.item:
        node.left=insert(node.left,item)
    else:
        node.right=insert(node.right,item)
    
    return node

def findMinVal(root):
    if root:
        while(root.left!=None):
            root=root.left
        return root.item   
    return None

def findMaxVal(root):
    if root:
        while(root.right!=None):
            root=root.right
        return root.item
    return None

root=None
root = insert(root, 8)
root = insert(root, 30)
root = insert(root, 15)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 40)

inorder(root)
print()
print('min val: ',findMinVal(root))
print('max val: ',findMaxVal(root))