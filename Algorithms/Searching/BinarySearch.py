def binarysearch(array,low,high,x):
    if(high>=low):
        mid=low+(high-low)//2
        if(array[mid]>x):
            return binarysearch(array,low,mid-1,x)
        elif(array[mid]<x):
            return binarysearch(array,mid+1,high,x)
        else:
            return "Found"
    else:
        return "Not Found"
