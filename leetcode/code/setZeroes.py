from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row0, col0 = False, False
        # 第一列是否有0
        for row in range(rows):
            if matrix[row][0] == 0:
                col0 = True
                break
        # 第一行是否有0
        for col in range(cols):
            if matrix[0][col] == 0:
                row0 = True
                break
        # 遍历矩阵
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = matrix[0][col] = 0
        # 若第一列的某个元素为0，则这一行，全部置0
        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(cols):
                    matrix[row][col] = 0
        # 若第一行的某个元素为0，则这一列，全部置0
        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(rows):
                    matrix[row][col] = 0

        if row0:
            for col in range(cols):
                matrix[0][col] = 0

        if col0:
            for row in range(rows):
                matrix[row][0] = 0


if __name__ == '__main__':
    data = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    so = Solution()
    so.setZeroes(matrix=data)
    print(data)
