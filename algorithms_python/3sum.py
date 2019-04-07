"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    
    n = len(nums)
    
    if n < 3:
        return []
    
    nums.sort()
    r = n - 1
    
    for i in range(n-2):
        l = i + 1
        r = n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            
            if not s and [nums[i], nums[l], nums[r]] not in res:
                res.append([nums[i], nums[l], nums[r]])
                
            if s > 0:
                r -= 1
            else:
                l += 1         
               
    return res 

nums = [-1, 0, 1, 2, -1, -4]

print (threeSum(nums))
