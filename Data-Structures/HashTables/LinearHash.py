class linear_hash:
	def __init__(self,size):
		self.size=size
		self.array=[None]*size
	def hashkey(self,value):
		return value%self.size
	def insert(self,data):
		key=self.hashkey(data)
		if(self.array[key]==None):
			self.array[key]=data
		else:
			i=key+1
			while(i!=key):
				if(self.array[i]==None):
					self.array[i]=data
					break
				i+=1
				if(i==self.size):
					i=0
				if(i==key):
					print("Not possible")
	def show(self):
		print(self.array)
