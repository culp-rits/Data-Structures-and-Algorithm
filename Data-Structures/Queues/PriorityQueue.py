class pnode:
    def __init__(self,key,data):
        self.data=data
        self.key=key

class priorityQ:
	def __init__(self):
		self.array=[]
	def insert(self,data):
		for i in range(len(self.array)):
			if(self.array[i].key>data.key):
				self.array.insert(i,data)
				return
		self.array.append(data)
	def delete(self):
		self.array.pop(0)
	def show(self):
		for i in self.array:
			print(i.data)
