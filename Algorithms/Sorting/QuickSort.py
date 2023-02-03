def quicksort(low,high,array):
    if(low<high):
        def part(low,high,array):
            j=low-1
            for i in range(low,high):
                if(array[i]<array[high]):
                    j+=1
                    array[j],array[i]=array[i],array[j]
            array[j+1],array[high]=array[high],array[j+1]
            return j+1
        piv=part(low,high,array)
        quicksort(low,piv-1,array)
        quicksort(piv+1,high,array)
