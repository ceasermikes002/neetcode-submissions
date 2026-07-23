class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Initialize pointers for nums1, nums2, and where to place in nums1
        i, j, k = m - 1, n - 1, m + n - 1

        # While there are elements in both nums1 and nums2
        while i >= 0 and j >= 0:
            # Place the larger element at the end of nums1
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If elements from nums2 are left, place them in nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1