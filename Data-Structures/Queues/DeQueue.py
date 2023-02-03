class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class dequeue:
    def __init__(self):
        self.head=None
        self.tail=None
    def isEmpty(self):
        if(self.head==None):
            print("True")
        else:
            print("False")
    def insertfront(self,data):
        temp=node(data)
        if(self.head==None):
            self.head=temp
            self.tail=temp
        else:
            temp.next=self.head
            self.head=temp
    def insertend(self,data):
        temp=node(data)
        if(self.head==None):
            self.head=temp
            self.tail=temp
        else:
            self.tail.next=temp
            self.tail=temp
    def deletefront(self):
        self.head=self.head.next
    def deletend(self):
        temp=self.head
        while(temp!=self.tail):
            if(temp.next==self.tail):
                self.tail=temp
                temp.next=None
                break
            temp=temp.next
    def display(self):
        temp=self.head                                
        while(temp!=None):                                 
            print(temp.data)           
            temp=temp.next                
    def search(self,data):
        temp=self.head
        while(temp.data!=data):
            temp=temp.next
            if(temp.data==data):
                print("Found")
                break
