#using last index as pivot element
#uses only 1 pointer i.e i , we use to collect the small values
#we use j for looping purpose
def partition(s,e,arr):
        pivot = arr[e]
        i = s
        for j in range(s,e):
               if arr[j]<pivot:
                    arr[i],arr[j] = arr[j],arr[i]
                    i+=1
        arr[i],arr[e] = arr[e],arr[i]
        return i
def quick_sort_lomuto(start,end,arr): 
        if start < end:
            pivot_loc = partition(start,end,arr)
            quick_sort_lomuto(start,pivot_loc-1,arr)
            quick_sort_lomuto(pivot_loc+1,end,arr)
arr = [18,45,17,93,5]
quick_sort_lomuto(0,len(arr)-1,arr)
print(arr)

# 3pointer approach
# as usual the last index is pivot value
