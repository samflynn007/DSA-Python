# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
nums = [3,2,2,3]
val = 3

# right = len(nums) - 1

def remove_element(nums,val):
    left = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[left] = nums[i] 
            left += 1
    return left

print(remove_element(nums,val))