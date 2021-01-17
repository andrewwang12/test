class Solution:
    def exist(self, board, word):
        if not board:
            return False
        row, column = len(board), len(board[0])
        # visited = [[False for i in range(column)] for j in range(row)]
        for i in range(row):
            for j in range(column):
                if self.dfs(board, word, i, j):
                    return True
        return False
    def dfs(self, board, word, i, j):
        if not word:
            return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = True
        res = self.dfs(board, word[1:], i, j - 1) or \
              self.dfs(board, word[1:], i, j + 1) or \
              self.dfs(board, word[1:], i + 1, j) or \
              self.dfs(board, word[1:], i - 1, j)
        board[i][j] = tmp
        return res

ans = Solution()
print(ans.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))