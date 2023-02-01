def insertionsort(array):
    for i in range(1,len(array)):
    #traversing all elements
        k=array[i]
        j=i
        while(j>0 and k<array[j-1]):
        #finding the correct insertion of element
            array[j]=array[j-1]
            j-=1
        array[j]=k
        #inserting element
