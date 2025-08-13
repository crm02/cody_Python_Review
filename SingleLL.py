from node import Node


# keep in mind the insert functions need to create a new node. 

class SLL:
    def __init__(self):
        self.head = None

    def insert_At_Begin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_At_Index(self,data,index):

        if index == 0:
            self.insert_At_Begin(data)
        position = 0
        current_node = self.head
        while (current_node != None and position +1 != index):
            current_node = current_node.next 
            position +=1
        if current_node!= None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next =new_node
        
        else:
            print('Index does not exists')

    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head == None:
            new_node = self.head
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def update_Node(self,data,index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = data # changed from src code
            return
        while current_node != None and position != index:
            position +=1
            current_node = current_node.next

        if current_node != None:
            current_node.data = data
        else:
            print('index not present')

    def remove_First_Node(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next    

    def remove_Last_Node(self):
        if self.head == None:
            return 
        else:
            current_node = self.head
            while current_node != None and current_node.next.next != None:
                current_node = current_node.next
            current_node.next = None
    
    def remove_At_Index(self,index):
        if self.head == None:
            return
        
        if index == 0:
            self.remove_First_Node()
            return

        current_node = self.head 
        position = 0

        while current_node != None and position +1 != index:
            current_node = current_node.next
            position+=1
        if current_node == None or current_node.next == None:
            print('Index not found')
        else:
            current_node.next = current_node.next.next

    def remove_Node(self,data):
        current_node = self.head
        if current_node.data == data:
            self.remove_First_Node()
            return
        while current_node != None and current_node.next.next.data != data:
            current_node = current_node.next
        
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next #DONT THINK THIS WORKS, LINE 100 SHOULD BE CURRENT.NEXT.DATA

            # THIS IS WHAT FINAL SRC CODE HAS
            ##while current_node is not None and current_node.next is not None:
            ##if current_node.next.data == data:
            ##    current_node.next = current_node.next.next
            ##    return
            ##current_node = current_node.next

    def sizeOfLL(self):
        size = 0
        current_node = self.head
        if self.head:
            while current_node:
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0 
    
    #is it possible to make a function that checks if SLL is empty? Had to retype that a lot
    def printLL(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next

# Now look over comments, import to new file, and complete tests