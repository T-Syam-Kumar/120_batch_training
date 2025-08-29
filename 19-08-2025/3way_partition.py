#quick sort using 3 pointers 
def _3way_pattition(start,end,arr):
    if start < end:
        lp = start
        i = start
        hp = end
        pivot = arr[end]
        while i <= hp:
            if arr[i]>pivot:
                arr[i],arr[hp] = arr[hp],arr[i]
                hp-=1
            elif arr[i]<pivot:
                arr[i],arr[lp] = arr[lp],arr[i]
                i+=1
                lp+=1
            else:
                i+=1
        _3way_pattition(start,lp-1,arr)
        _3way_pattition(hp+1,end,arr)
arr = [23,7,8,34,89,345,76]
_3way_pattition(0,len(arr)-1,arr)
print(arr)
