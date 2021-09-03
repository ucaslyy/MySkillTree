from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        方法一：使用最朴素的做法，已知两个数组的有效长度，因此从数组末尾开始遍历，使用三个指针记录2个旧数组位置、1个新数组位置。
        """
        index = m + n - 1
        mi = m - 1
        ni = n - 1
        while mi >= 0 and ni >= 0:
            if nums1[mi] > nums2[ni]:
                nums1[index] = nums1[mi]
                mi -= 1
            else:
                nums1[index] = nums2[ni]
                ni -= 1
            index -= 1

        while mi >= 0:
            nums1[index] = nums1[mi]
            index -= 1
            mi -= 1

        while ni >= 0:
            nums1[index] = nums2[ni]
            index -= 1
            ni -= 1
