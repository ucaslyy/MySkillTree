from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = 9
        # 数字 1-9 在每一行只能出现一次。
        for r in range(length):
            tmp = set()
            for c in range(length):
                if board[r][c] in tmp:
                    return False
                elif board[r][c] == '.':
                    continue
                else:
                    tmp.add(board[r][c])

        # 数字 1-9 在每一列只能出现一次。
        for c in range(length):
            tmp = set()
            for r in range(length):
                if board[r][c] in tmp:
                    return False
                elif board[r][c] == '.':
                    continue
                else:
                    tmp.add(board[r][c])

        # 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
        step = 3
        for r in range(0, length, step):
            for c in range(0, length, step):
                tmp = set()
                for i in range(r, r+step):
                    for j in range(c, c+step):
                        if board[i][j] in tmp:
                            return False
                        elif board[i][j] == '.':
                            continue
                        else:
                            tmp.add(board[i][j])

        return True
