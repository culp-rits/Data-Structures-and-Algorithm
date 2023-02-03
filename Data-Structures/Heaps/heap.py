class heap:
	def __init__(self,data):
		self.arr=data
	def minheapify(self,i):
		l=2*i+1
		r=2*(i+1)
		if(l<len(self.arr) and self.arr[l]<self.arr[i]):
			min=l
		else:
			min=i
		if(r<len(self.arr) and self.arr[r]<self.arr[min]):
			min=r
		if(min!=i):
			self.arr[min],self.arr[i]=self.arr[i],self.arr[min]
			self.minheapify(min)
	def minbuild(self):
		n=(len(self.arr)//2)-1
		for i in range(n,-1,-1):
			self.minheapify(i)
	def minadd(self,data):
		self.arr.append(data)
		self.minbuild()
	def remmin(self):
		self.arr.pop(0)
		self.minbuild()
	def maxheapify(self,i):
		l=2*i+1
		r=2*(i+1)
		if(l<len(self.arr) and self.arr[l]>self.arr[i]):
			max=l
		else:
			max=i
		if(r<len(self.arr) and self.arr[r]>self.arr[max]):
			max=r
		if(max!=i):
			self.arr[max],self.arr[i]=self.arr[i],self.arr[max]
			self.maxheapify(max)
	def maxbuild(self):
		n=(len(self.arr)//2)-1
		for i in range(n,-1,-1):
			self.maxheapify(i)
	def maxadd(self,data):
		self.arr.append(data)
		self.maxbuild()
	def remmax(self):
		self.arr.pop(0)
		self.maxbuild()
	def show(self):
		print(self.arr)
