from leetcode.code.containsDuplicate import Solution as containsDuplicate_Solution
from leetcode.code.maxSubArray import Solution as maxSubArray_Solution
from leetcode.code.twoSum import Solution as TwoSumSolution
from leetcode.code.merge import Solution as MergeSolution
from leetcode.code.intersect import Solution as IntersectSolution
from leetcode.code.maxProfit import Solution as MaxProfitSolution


def test_max_profit():
    data = [
        [[7, 1, 5, 3, 6, 4]],
        [[7, 6, 4, 3, 1]],
    ]
    for item in data:
        so = MaxProfitSolution()
        res = so.maxProfit(prices=item[0])
        print(res)


def test_intersect():
    data = [
        [[1, 2, 2, 1], [2, 2]],
        [[4, 9, 5], [9, 4, 9, 8, 4]],
    ]
    for item in data:
        so = IntersectSolution()
        res = so.intersect(nums1=item[0], nums2=item[1])
        print(res)


def test_merge():
    data = [
        [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
        [[1], 1, [], 0],
    ]
    for item in data:
        so = MergeSolution()
        so.merge(nums1=item[0], m=item[1], nums2=item[2], n=item[3])
        print(item[0])


def test_containsDuplicate():
    data = [
        [[1, 2, 3, 1]],
        [[1, 2, 3, 4]],
        [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]
    ]

    for item in data:
        so = containsDuplicate_Solution()
        print(so.containsDuplicate(nums=item[0]))


def test_maxSubArray():
    data = [
        [[-2, 1, -3, 4, -1, 2, 1, -5, 4]],
        [[1]],
        [[0]],
        [[-1]],
        [[-100000]]
    ]
    for item in data:
        so = maxSubArray_Solution()
        print(so.maxSubArray(nums=item[0]))


def test_two_sum():
    data = [
        [[2, 7, 11, 15], 9],
        [[3, 2, 4], 6],
        [[3, 3], 6],
    ]
    for item in data:
        so = TwoSumSolution()
        print(so.twoSum(nums=item[0], target=item[1]))


if __name__ == '__main__':
    # test_containsDuplicate()
    # test_maxSubArray()
    # test_two_sum()
    # test_merge()
    # test_intersect()
    test_max_profit()
