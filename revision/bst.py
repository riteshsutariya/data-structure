class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left=None
        self.right=None
        
    def __str__(self) -> str:
        leftVal=''
        rightVal='' 
        if self.left is not None:
            leftVal=str(self.left.val)
        if self.right is not None:
            rightVal=str(self.right.val)       
        if self.left is None:
            leftVal='None'
        if self.right is None:
            rightVal='None'
        return leftVal+'<-'+str(self.val)+'->'+rightVal


def insert(root,val):
    if root is None:
        return Node(val)
    if root.val>val:
        root.left=insert(root.left,val)
    elif root.val<val:
        root.right=insert(root.right,val)
    return root

def traverse_inorder(root):
    if root is not None:
        traverse_inorder(root.left)
        print(root.val,end='->')
        traverse_inorder(root.right)

def traverse_preorder(root):
    if root is not None:
        print(root.val,end='->')
        traverse_preorder(root.left)
        traverse_preorder(root.right)
        
def traverse_postorder(root):
    if root is not None:
        traverse_postorder(root.left)
        traverse_postorder(root.right)
        print(root.val,end='->')

def search(root,val):
    if root is None or root.val==val:
        return root
    if val<root.val:
        return search(root.left,val)
    else:
        return search(root.right,val)

def find_min(root):
    if root is None:
        return root
    while root.left is not None:
        root=root.left
    return root

def find_max(root):
    if root is None:
        return root
    while(root.right is not None):
        root=root.right
    return root

# def delete(root,val):
#     if root is None:
#         return root
#     if val<root.val:
#         root.left=delete(root.left,val)
#     elif val>root.val:
#         root.right=delete(root.right,val)
#     else:
#         if root.left is None:
#             temp=root.right
#             del root
#             return temp
#         elif root.right is None:
#             temp=root.left
#             del root
#             return temp
#         else:
#             temp=find_max(root.left)
#             root.val=temp.val
#             root.left=delete(root.left,temp.val)
#     return root    


def delete(root,val):
    if root is not None:
        if val<root.val:
            root.left=delete(root.left,val)
        elif val>root.val:
            root.right=delete(root.right,val)
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
                temp=find_min(root.right)
                root.val=temp.val
                root.right=delete(root.right,temp.val)
    return root
root=None

root=insert(root,100)
root=insert(root,120)
root=insert(root,180)
root=insert(root,80)
root=insert(root,160)
root=insert(root,250)
root=insert(root,110)
root=insert(root,105)
root=insert(root,60)
root=insert(root,85)
root=insert(root,45)
root=insert(root,25)
root=insert(root,50)

print(root.left.val)

# print("min: ",find_min(None))
# print("max: ",find_max(None))

# print('pre order traversal:-')
# traverse_preorder(root)
# print('')


print('in order traversal:-')
traverse_inorder(root)
print('')

delete(root,120)

print('in order traversal:-')
traverse_inorder(root)
print('')

# print('post order traversal:-')
# traverse_postorder(root)
# print('')


# result=search(root,100)
# if result is None:
#     print('node not found!')
# else:
#     print('node found in tree.')


