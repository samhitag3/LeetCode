class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1Copy = list(nums1)
        i = 0
        j = 0
        k = 0
        while i < m or j < n:
            if i == m:
                nums1[k] = nums2[j]
                j += 1
            elif j == n:
                nums1[k] = nums1Copy[i]
                i += 1
            elif nums1Copy[i] <= nums2[j]:
                nums1[k] = nums1Copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        