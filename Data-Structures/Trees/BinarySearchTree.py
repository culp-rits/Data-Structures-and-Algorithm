class tnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,data):
        if(root.data>data):
            if(root.left==None):
                root.left=tnode(data)
            else:
                self.insert(root.left,data)
        else:
            if(root.right==None):
                root.right=tnode(data)
            else:
                self.insert(root.right,data)
    def search(self,root,data):
        if(root.data==data):
            return root
        elif(root.data>data):
            return self.search(root.left,data)
        else:
            return self.search(root.right,data)
    def delete(self,root,data):
        if(root==None):
            return root
        if(data<root.data):
            root.left=self.delete(root.left,data)
        elif(data>root.data):
            root.right=self.delete(root.right,data)
        else:
            if(root.left==None):
                temp=root.right
                root=None
                return temp
            elif(root.right==None):
                temp = root.left
                root = None
                return temp
            temp = self.minnode(root.right)
            root.data=temp.data
            root.right=self.delete(root.right,temp.data)
        return root
    def minnode(self,root):
        temp=root
        while(temp.left!=None):
            temp=temp.left
        return temp
    def show(self,root):
        if(root!=None):
            self.show(root.left)
            print(root.data,"->",end="")
            self.show(root.right)
