class quad_hash:
	def __init__(self,size):
		self.size=size
		self.array=[None]*size
	def hashkey(self,value):
		return value%self.size
	def insert(self,data):
		key=self.hashkey(data)
		i=1
		if(self.array[key]==None):
			self.array[key]=data
		else:
			while(i<self.size):
				if(self.array[(data+i**2)%7]==None):
					self.array[(data+i**2)%7]=data
					break
				i+=1
				if(i==self.size):
					print(data,"Not possible")
	def show(self):
		print(self.array)
