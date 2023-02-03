def shellsort(array):
    int=len(array)//2
    while(int>0):
        for i in range(int,len(array)):
            k=array[i]
            j=i
            while(j>=int and k<array[j-int]):
                array[j]=array[j-int]
                j-=int
            array[j]=k
        int//=2
