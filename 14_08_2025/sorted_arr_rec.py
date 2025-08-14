def sort_arr(nums,i):
    if i == len(nums)-1:
        return True
    if nums[i]<nums[i+1]:
        return sort_arr(nums,i+1)
nums = [1,2,34,56]
print("True" if sort_arr(nums,0) else "false")