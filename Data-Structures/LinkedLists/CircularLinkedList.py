class node:
    def __init__(self,data):
        self.data=data
        self.next=None
 
class circularlinkedlist:
    def __init__(self):
        self.cursor=None
    def insert(self,data):
        if(self.cursor==None):
            self.cursor=node(data)
            self.cursor.next=self.cursor
        else:
            temp=node(data)
            temp.next=self.cursor.next
            self.cursor.next=temp
            self.cursor=temp
    def delete(self,data):
        temp=self.cursor
        while(temp.data!=data):
            if(temp.next.data==data):
                temp.next=temp.next.next
                break
            temp=temp.next
    def search(self,data):
        temp=self.cursor
        while(temp.data!=data):
            temp=temp.next
            if(temp.data==data):
                print("Found")
                break
    def display(self):
        temp=self.cursor
        print(temp.data)
        temp=temp.next
        while(temp.data!=self.cursor.data):
            print(temp.data)
            temp=temp.next
