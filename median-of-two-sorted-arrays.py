class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArr = []
        i,j = 0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] <= nums2[j]:
                mergedArr.append(nums1[i])
                i+=1
            else:
                mergedArr.append(nums2[j])
                j+=1
        for m in range(i,len(nums1)):
            mergedArr.append(nums1[m])
        for m in range(j,len(nums2)):
            mergedArr.append(nums2[m])
        if len(mergedArr) % 2 == 0:
            middleIndex = len(mergedArr) // 2
            return (mergedArr[middleIndex - 1] + mergedArr[middleIndex]) / 2
        else:
            middleIndex = int((len(mergedArr)-1)//2)
            return mergedArr[middleIndex]
