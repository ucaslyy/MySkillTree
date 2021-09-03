from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     tmp_dict = {}
    #     for index, value in enumerate(nums):
    #         if value in tmp_dict:
    #             tmp_dict[value].append(index)
    #         else:
    #             tmp_dict[value] = [index]
    #
    #     ans = []
    #     for key in tmp_dict.keys():
    #         if target - key == key and len(tmp_dict[key]) > 1:
    #             ans = tmp_dict[key][0:2]
    #             break
    #         elif target - key != key and target - key in tmp_dict:
    #             ans.append(tmp_dict[key][0])
    #             ans.append(tmp_dict[target - key][0])
    #             break
    #     return ans

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        方法一: 一次循环搞定。每一次循环，均需要判断一下当前数值与目标target的差值是否已经存在。
               若存在，则当前数值的下标和差值的下标就是所求答案。若不存在，则按照键值对 key: value = 当前数值：当前下标 存储字典。
        :param nums:
        :param target:
        :return:
        """
        tmp_dict = {}
        ans = []
        for index, value in enumerate(nums):
            if target - value in tmp_dict:
                ans.append(tmp_dict[target - value])
                ans.append(index)
                break
            else:
                tmp_dict[value] = index

        return ans
