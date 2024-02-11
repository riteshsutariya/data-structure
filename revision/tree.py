class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None
        pass

def traverse(root):
    if root is not None:
        traverse(root.left)
        print(root.val,end='->')
        traverse(root.right)

root=Node(10)
root.left=Node(15)
root.left.right=Node(45)
root.left.left=Node(58)
root.left.left.left=Node(200)
root.left.left.left.left=Node(400)
root.left.left.left.left.right=Node(580)
root.right=Node(25)
root.right.left=Node(48)
root.right.right=Node(57)
root.right.right.left=Node(96)
root.right.left.left=Node(98)
root.right.left.left.right=Node(100)


traverse(root)