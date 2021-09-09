from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        # 遍历数组nums1，建立键值对，key=数值，value=出现次数
        tmp_dict = {}
        for num in nums1:
            tmp_dict[num] = tmp_dict[num] + 1 if num in tmp_dict else 1

        # 遍历数组nums2，若在临时数组中出现，则表明此数是交集，同时value减1；
        # 当value为0时，将key值剔除。
        for num in nums2:
            if num in tmp_dict:
                ans.append(num)
                tmp_dict[num] -= 1
                if tmp_dict[num] == 0:
                    tmp_dict.pop(num)

        return ans
