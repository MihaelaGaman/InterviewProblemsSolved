"""
Median of two sorted arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if len(nums1) < len(nums2):
        n = len(nums1)
        m = len(nums2)
        a = nums1
        b = nums2
    else:
        n = len(nums2)
        m = len(nums1)
        a = nums2
        b = nums1
    median = 0
    i = 0
    j = 0
    min_index = 0 
    max_index = n
   
    while (min_index <= max_index) : 
  
        i = int((min_index + max_index) / 2) 
        j = int(((n + m + 1) / 2) - i) 
   
        # i == n => no elements from a in the second half
        # j == 0 => no elements from b in the first half 
        # Searching on right 
        if (i < n and j > 0 and b[j - 1] > a[i]) : 
            min_index = i + 1
               
        # i = 0 => no elements from a in the first half 
        # j = m => no elements from b in the second half
        # Searching on left 
        elif (i > 0 and j < m and b[j] < a[i - 1]) : 
            max_index = i - 1
       
        # here we have the halves searched for 
        else : 
      
            # no elements from nums1 in the first half
            # => return the last element in b  
            if (i == 0) : 
                median = b[j - 1] 

            # no elements in the first half from b
            # => return the last element in a
            elif (j == 0) : 
                median = a[i - 1]          
            else : 
                median = max(a[i - 1], b[j - 1])  
            break
     
    # Compute the median. 
    # odd no of elems => one middle element
    if ((n + m) % 2 == 1) : 
        return median 

    # no elems from a in the second half  
    if (i == n) : 
        return ((median + b[j]) / 2.0) 

    # no elems from b in the second half 
    if (j == m) : 
        return ((median + a[i]) / 2.0) 

    return ((median + min(a[i], b[j])) / 2.0)


# Test 1
nums1 = [1, 3]
nums2 = [2]

print "Test1: ", findMedianSortedArrays(nums1, nums2)

# Test 2
nums1 = [1, 2]
nums2 = [3, 4]


print "Test2: ", findMedianSortedArrays(nums1, nums2)

