class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        res = 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        res += 1
                    else:
                        elem_val = min(matrix[r-1][c-1], matrix[r][c-1], matrix[r-1][c]) + matrix[r][c]
                        res += elem_val
                        matrix[r][c] = elem_val
        return res

"""

"""