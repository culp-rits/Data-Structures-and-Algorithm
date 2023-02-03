class hash:
	def __init__(self,size):
		self.size=size
		self.array=[None]*size
	def hashkey(self,value):
		return value%self.size
	def insert(self,data):
		self.array[self.hashkey(data)]=data
	def show(self):
		print(self.array)
