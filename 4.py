def findMedian(nums1, nums2): 
    mid = 0
    mid_idx = 0
    length = len(nums1) + len(nums2)
    if length % 2 != 0:
        if(len(nums1) > len(nums2)): 
            mid = nums1[length // 2]
        elif(len(nums1) < len(nums2)): 
            mid_idx = (length // 2) - len(nums1)
            mid = nums2[mid_idx]
    else: 
        if(len(nums1) < len(nums2)): 
            mid_idx = length // 2 - (len(nums1))   
            mid = (nums2[mid_idx - 1] + nums2[mid_idx]) // 2
        elif(len(nums1) > len(nums2)): 
            mid = (nums1[(length // 2) - 1] + nums1[length // 2]) // 2
    return mid
# print(findMedian([1, 2, 3, 4, 7, 8, 10], [3, 4, 6, 8, 9, 12]))
# print(findMedian([1, 2, 3], [3, 4, 6, 8, 9]))

# print(findMedian([1, 2, 3, 6, 7, 20, 21], [3, 4, 6, 8, 9]))
print(findMedian([1,3], [2]))

                  