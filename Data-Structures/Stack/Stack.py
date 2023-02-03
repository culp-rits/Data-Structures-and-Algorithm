class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        if(self.top==None):
            self.top=node(data)
        else:
            temp=node(data)
            temp.next=self.top
            self.top=temp
    def pop(self):
        temp=self.top
        self.top=self.top.next
        return temp.data
    def peek(self):
        if(self.top!=None):
            return self.top.data
        else: 
            return None
