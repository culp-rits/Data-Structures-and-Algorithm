class dnode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class doublylinkedlist:
    def __init__(self):
        self.cursor=None
    def insertfront(self,data):
        if(self.cursor==None):
            self.cursor=dnode(data)
        else:
            temp=dnode(data)
            self.cursor.prev=temp
            temp.next=self.cursor
            self.cursor=temp
    def insertend(self,data):
        temp=self.cursor
        while(temp!=None):
            if(temp.next==None):
                tmp=dnode(data)
                temp.next=tmp
                tmp.prev=temp
                break
            temp=temp.next
    def insertpos(self,data,pos):
        temp=self.cursor
        while(pos-2):
            pos-=1
            temp=temp.next
        tmp=dnode(data)
        tmp.next=temp.next
        tmp.prev=temp
        temp.next=tmp
        tmp.next.prev=tmp
    def deletefront(self):
        self.cursor=self.cursor.next
        self.cursor.prev=None
    def deletend(self):
        temp=self.cursor
        tmp=self.cursor.next
        while(tmp.next!=None):
            tmp=tmp.next
            temp=temp.next
            if(tmp.next==None):
                temp.next=None
                tmp.prev=None
    def deletedata(self,data):
        temp=self.cursor
        if(temp.data==data):
            self.cursor=self.cursor.next
            self.cursor.prev=None
        else:
            tmp=self.cursor.next
            while(tmp!=None):
                if(tmp.data==data):
                    temp.next=tmp.next
                    tmp.next.prev=temp
                    break
                tmp=tmp.next
                temp=temp.next
    def search(self,data):
        temp=self.cursor
        i=1
        while(temp!=None):
            if(temp.data==data):
                print(i)
                break
            i+=1
            temp=temp.next
    def display(self):
        temp=self.cursor
        while(temp!=None):
            print(temp.data)
            if(temp.next==None):
                tmp=temp
            temp=temp.next
