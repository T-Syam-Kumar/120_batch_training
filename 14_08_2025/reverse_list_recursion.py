#using index
def reverse_list(nums,n):
    if len(nums) !=  0:
        return reverse_list(nums,n-1)  
    print(nums[n])
nums = [5,2,3,4,5]
n = len(nums)-1
reverse_list(nums,n)