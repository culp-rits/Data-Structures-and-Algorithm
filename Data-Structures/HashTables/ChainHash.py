class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.cursor=None
    def insertfront(self,data):
        if(self.cursor==None):
            self.cursor=node(data)
        else:
            temp=node(data)
            temp.next=self.cursor
            self.cursor=temp
    def insertend(self,data):
        temp=self.cursor
        while(temp!=None):
            if(temp.next==None):
                temp.next=node(data)
                break
            temp=temp.next
    def insertpos(self,data,pos):
        temp=self.cursor
        while(pos-2):
            pos-=1
            temp=temp.next
        tmp=node(data)
        tmp.next=temp.next
        temp.next=tmp
    def deletefront(self):
        self.cursor=self.cursor.next
    def deletend(self):
        temp=self.cursor
        tmp=self.cursor.next
        while(tmp.next!=None):
            tmp=tmp.next
            temp=temp.next
            if(tmp.next==None):
                temp.next=None
    def deletedata(self,data):
        temp=self.cursor
        if(temp.data==data):
            self.cursor=self.cursor.next
        else:
            tmp=self.cursor.next
            while(tmp!=None):
                if(tmp.data==data):
                    temp.next=tmp.next
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
            temp=temp.next
            
class chain_hash:
	def __init__(self,size):
		self.size=size
		self.array=[None]*size
	def hashkey(self,value):
		return value%self.size
	def insert(self,data):
		key=self.hashkey(data)
		if(self.array[key]==None):
			self.array[key]=linkedlist()
			self.array[key].insertfront(data)
		else:
			self.array[key].insertend(data)
	def show(self):
		for i in self.array:
			if(i!=None):
				i.display()
				print("\n")
			else:
				print(i,"\n")
