class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Step 1: Merge both sorted arrays into one
        merged = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
                
        # Append any remaining elements
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        # Step 2: Find the median
        n = len(merged)
        if n % 2 == 1:
            # note here index start from 0 
            return float(merged[n // 2])
        else:
            # same index starts from 0
            return (merged[(n // 2) - 1] + merged[n // 2]) / 2.0