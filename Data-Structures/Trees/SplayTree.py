class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def splay(self, n):
        while n.parent != None:
            if n.parent == self.root:
                if n == n.parent.left:
                    self.rightRotate(n.parent)
                else:
                    self.leftRotate(n.parent)
            else:
                p = n.parent
                g = p.parent
                if n.parent.left == n and p.parent.left == p: 
                    self.rightRotate(g)
                    self.rightRotate(p)
                elif n.parent.right == n and p.parent.right == p: 
                    self.leftRotate(g)
                    self.leftRotate(p)
                elif n.parent.right == n and p.parent.left == p:
                    self.leftRotate(p)
                    self.rightRotate(g)
                elif n.parent.left == n and p.parent.right == p:
                    self.rightRotate(p)
                    self.leftRotate(g)

    def insert(self, n):
        y = None
        temp = self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        n.parent = y
        if y == None:
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n
        self.splay(n)

    def preOrder(self, n):
        if n != None:
            print(n.data)
            self.inOrder(n.left)
            self.inOrder(n.right)
