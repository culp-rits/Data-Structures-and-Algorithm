def heapsort(array):
	def maxheapify(array,n,i):
		l=2*i+1
		r=2*(i+1)
		if(l<n and array[l]>array[i]):
			max=l
		else:
			max=i
		if(r<n and array[r]>array[max]):
			max=r
		if(max!=i):
			array[max],array[i]=array[i],array[max]
			maxheapify(array,n,max)
	for i in range(len(array)//2-1,-1,-1):
		maxheapify(array,len(array),i)
	for i in range(len(array)-1,0,-1):
		array[i],array[0]=array[0],array[i]
		maxheapify(array,i,0)
