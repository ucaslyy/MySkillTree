from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        方法一：动态规划，当前的子序列和加上下一个数大于下一个数本身时，则说明下一个数加入子序列比不加入可以获得更大的子序列和。
               每个子序列和都和之前最大的子列和比较，更新最大值。
        :param nums:
        :return:
        """
        max_sum = tmp_sum = nums[0]
        for num in nums[1:]:
            tmp_sum = max(tmp_sum + num, num)
            max_sum = max(max_sum, tmp_sum)

        return max_sum
