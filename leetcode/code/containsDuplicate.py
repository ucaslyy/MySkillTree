from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        方法一：遍历数组，并采用临时数组将遍历过的数值记录。
              当出现重复值时，则终止遍历返回True；
              当循环结束时，仍无重复数字出现，则返回False。
        :param nums:
        :return:
        """
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        """
        方法二：分别计算数组转换为集合前后的长度，因为集合的元素时不能重复的；
               因此若长度相等，则数组无重复数据，若长度不等，则数据存在重复数据。
        :param nums:
        :return:
        """
        return not (len(nums) == len(set(nums)))
