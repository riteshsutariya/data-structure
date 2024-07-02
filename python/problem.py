class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverse(node):
    while node is not None:
        if node.next is None:
            print(node.data)
        else:
            print(node.data, end= '->')
        node = node.next
        
def traverse_unique(node):
    if node is not None:
        if node.next is None:
            print(node.data, end='->')
        else:
            # traverse list till middle
            temp = node
            q = []
            stack = []
            
            while temp is not None and temp.next is not None:
                q.append(node.data)
                node = node.next
                temp = temp.next.next 
            
            while node is not None:
                stack.append(node.data)
                node = node.next
                
            while q or stack:
                if q:
                    print(q.pop(0), end='->')
                if stack:
                    print(stack.pop(), end='->')
            
            # print('stack: ',stack)
            # print('q: ',q)
                
            # while len(stack) > 0 and len(q) > 0:
            #     print(q.pop(0), end='->')
            #     print(stack.pop(), end='->')
            
            # while len(q) > 0:
            #     print(q.pop(0), end='->')   
            
            # while len(stack) > 0:
            #     print(stack.pop(), end='->')
                
        
node1 = Node(54)
node2 = Node(55)
node3 = Node(32)
node4 = Node(31)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
# node4.next = node5

traverse(node1)

traverse_unique(node1)