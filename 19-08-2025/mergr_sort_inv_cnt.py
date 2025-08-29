#merge sort with inversion count
def merge_sort_inversion(nums):
    if len(nums)<=1:
        return 0,nums
    mid = len(nums)//2
    li , left = merge_sort_inversion(nums[:mid])
    ri , right = merge_sort_inversion(nums[mid:])
    mi , merged_list = merge(left,right)
def merge(left,right):
    i = 0
    j = 0
    mi = 1
    merged_list = [] 
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged_list.append(left[i])
            i+=1
        else:
            pass 