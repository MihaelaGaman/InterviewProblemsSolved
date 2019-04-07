"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return [[nums[i]] + permuted_nums \
           for i in range(len(nums)) 
           for permuted_nums in permute(nums[:i] + nums[i+1:])] or [nums]


"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1


Solution:
Wikipedia describes the following algorithm by Narayana Pandit that changes the list in-place to generate the next lexicographic permutation.

1. Find the largest index i such that L[i] < L[i + 1]. If no such index exists, the permutation is the last permutation.
2. Find the largest index j greater than i such that L[j] > L[i].
3. Swap the value of L[i] with that of L[j].
4. Reverse the sequence from L[i + 1] up to and including the final element L[n - 1], where L is zero-indexed.

"""

def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    largest_i = -1
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            largest_i = i
            break

    if largest_i == -1:
        nums.sort()
    else:
        for j in range(n-1, largest_i, -1):
            if nums[j] > nums[largest_i]:
                aux = nums[j]
                nums[j] = nums[largest_i]
                nums[largest_i] = aux
                break

            l = nums[largest_i + 1:]
            for k in range(len(l)):
                nums[largest_i + 1 + k] = l[len(l) - 1 - k]

def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result_perms = [[]]
    for n in nums:
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm)+1):
                np = perm[:i] + [n] + perm[i:]
                if np not in result_perms:
                    new_perms.append(np)
                    result_perms = new_perms
    return result_perms


print(permute([1, 2, 3]))

nums = [1, 5, 1]
nextPermutation(nums)
print nums
