class node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None
		self.height = 0

class avl:
	def insert(self,root,data):
		if(root == None):
			return node(data)
		elif(data > root.data):
			root.right =  self.insert(root.right,data)
		elif(data < root.data):
			root.left = self.insert(root.left,data)
		return self.balance(root)

	def delete(self,root,data):
		if(root == None):
			return
		elif(data > root.data):
			root.right = self.delete(root.right,data)
		elif(data < root.data):
			root.left = self.delete(root.left,data)
		else:
			if(root.left == None):
				temp = root.right
				root = None
				return temp
			elif(root.right == None):
				temp = root.left
				root = None
				return temp
			else:
				temp = self.inorder(root.right)
				root.data = temp.data
				root.right = self.delete(root.right,data)
		return self.balance(root)

	def balance(self,root):
		root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
		balance_factor = self.get_balance_factor(root)
		if(balance_factor > 1 and self.get_balance_factor(root.left)>=0):
			return self.right_rotate(root)
		if(balance_factor < -1 and self.get_balance_factor(root.right)<=0):
			return self.left_rotate(root)
		if(balance_factor > 1 and self.get_balance_factor(root.left)<0):
			root.left = self.left_rotate(root.left)
			return self.right_rotate(root)
		if(balance_factor < -1 and self.get_balance_factor(root.right)>0):
			root.right = self.right_rotate(root.right)
			return self.left_rotate(root)
		return root
		
	def left_rotate(self,root):
		temp1 = root.right
		temp2 = temp1.left
		temp1.left = root
		root.right = temp2
		root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
		temp1.height =  1 + max(self.get_height(temp1.left),self.get_height(temp1.right))
		return temp1

	def right_rotate(self,root):
		temp1 = root.left
		temp2 = temp1.right
		temp1.right = root
		root.left = temp2
		root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
		temp1.height =  1 + max(self.get_height(temp1.left),self.get_height(temp1.right))
		return temp1

	def get_balance_factor(self,root):
		return self.get_height(root.left)-self.get_height(root.right)

	def get_height(self,root):
		if(root == None):
			return 0
		else:
			return root.height
	
	def inorder(self,root):
		if(root.left == None):
			return root
		else:
			return self.inorder(root.left)

	def show(self,root):
		if(root != None):
			print(root.data,end = " ")
			self.show(root.left)
			self.show(root.right)
