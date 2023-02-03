class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):                                 
        self.head=None              
        self.tail=None                                  
    def empty(self):                                     
        if(self.head==None):                                
            print("True")
        else:
            print("False")
    def enqueue(self,data):                             
        temp=node(data)                                  
        if(self.empty()==True):                         
            self.tail=temp
            self.head=temp
        else:                              
            self.tail.next=temp                           
            self.tail=temp                              
    def dequeue(self):
        if(self.empty()==False):                        
            self.head=self.head.next                        
    def next(self):
        if(self.empty()==False):                        
            print(self.head.data)     
    def display(self):
        temp=self.head                                
        while(temp!=None):                                 
            print(temp.data)           
            temp=temp.next
