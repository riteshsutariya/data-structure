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

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)

print()