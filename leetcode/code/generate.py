from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1, 1]]
        if numRows == 1 or numRows == 2:
            return ans[0: numRows]
        else:
            for num in range(3, numRows + 1):
                tmp = [1] * num
                for i in range(1, len(ans[-1])):
                    tmp[i] = ans[-1][i - 1] + ans[-1][i]
                ans.append(tmp)
        return ans


if __name__ == '__main__':
    so = Solution()
    so.generate(numRows=5)
