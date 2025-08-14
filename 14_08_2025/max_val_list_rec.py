def find_min(index,nums):
    if index == len(nums)-1:
        return nums[index]
    max = find_min(index+1,nums)
    return nums[index] if nums[index]>max else max
nums = [5,3,12,8,4]
print(find_min(0,nums))