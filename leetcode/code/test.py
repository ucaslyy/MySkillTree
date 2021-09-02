from leetcode.code.containsDuplicate import Solution as containsDuplicate_Solution
from leetcode.code.maxSubArray import Solution as maxSubArray_Solution


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


if __name__ == '__main__':
    # test_containsDuplicate()
    test_maxSubArray()
