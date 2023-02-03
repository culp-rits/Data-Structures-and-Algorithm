def mergesort(array):
    if(len(array)>1):
        n=len(array)//2
        l=array[:n]
        r=array[n:]
        mergesort(l)
        mergesort(r)
        i=0
        while(l!=[] and r!=[]):
            if(l[0]<r[0]):
                array[i]=l.pop(0)
            else:
                array[i]=r.pop(0)
            i+=1
        while(l!=[]):
            array[i]=l.pop(0)
            i+=1
        while(r!=[]):
            array[i]=r.pop(0)
            i+=1
