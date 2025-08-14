def sum_of_arr(index,nums,n):
    if index == n:
        return nums[index]
    return nums[index]+sum_of_arr(index+1,nums,n)
nums = [1,2,3,4,5]
n = len(nums)
index = 0
res = sum_of_arr(index,nums,len(nums)-1)
print(res)
# Slicing 
def sum_slicing(nums):
    if not nums:
        return 0 
    return nums[0]+sum_slicing(nums[1:])
nums = [1,2,3,4,5,6]
print(sum_slicing(nums))
#method 2
def sum_slicing(nums):
    if len(nums) == 1:
        return nums[0] 
    return nums[0]+sum_slicing(nums[1:])
nums = [1,2,3,4,5,6,7]
print(sum_slicing(nums))



