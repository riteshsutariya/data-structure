class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertAtBegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
            
    def insertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next
            
        current_node.next=new_node
        
    def printLL(self):
        current_node=self.head
        while(current_node):
            print(current_node.data)
            current_node=current_node.next
            
linkedlist=LinkedList()

linkedlist.insertAtBegin('R')
linkedlist.insertAtEnd('I')
linkedlist.insertAtEnd('T')
linkedlist.insertAtEnd('E')
linkedlist.insertAtEnd('S')
linkedlist.insertAtEnd('H')
linkedlist.insertAtBegin('T')

linkedlist.printLL()