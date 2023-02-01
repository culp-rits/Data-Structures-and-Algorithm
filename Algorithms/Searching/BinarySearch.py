def binarysearch(array,low,high,x):
    if(high>=low):
    #making sure the element is not searched
        mid=low+(high-low)//2
        #computing mid element to be searched
        if(array[mid]>x):
            return binarysearch(array,low,mid-1,x)
            #recursive call on left subarray 
        elif(array[mid]<x):
            return binarysearch(array,mid+1,high,x)
            #recursive call on right subarray
        else:
            return "Found"
            #element found
    else:
        return "Not Found"
        #element is not present
