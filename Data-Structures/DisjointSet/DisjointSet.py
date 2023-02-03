class disjointset:
    def __init__(self):
        self.arr={}
    def make(self,i):
        self.arr[i]=i
    def find(self,x):
        if(self.arr[x]==x):
            return x
        else:
            return self.find(self.arr[x])
    def union(self,x,y):
        a=self.find(x)
        b=self.find(y)
        self.arr[a]=b 
    def show(self):
        print(self.arr)
