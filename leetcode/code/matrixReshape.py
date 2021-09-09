from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        new_mat = [[0] * c for _ in range(r)]
        p, q = 0, 0
        for i in range(m):
            for j in range(n):
                new_mat[p][q] = mat[i][j]
                q += 1
                if q == c:
                    p, q = p + 1, 0

        return new_mat
