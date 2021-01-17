class Solution:
    def combine(self, n, k):
        res, combo = [], []
        if n <= 0 or k <= 0:
            return res
        self.findCombo(res, n, k, 1, combo)
        return res
    def findCombo(self, res, n, k, i, combo):
        if k == 0:
            res.append(combo.copy())
        elif i + k - 1 <= n:
            combo.append(i)
            self.findCombo(res, n, k - 1, i + 1, combo)
            combo.pop()
            self.findCombo(res, n, k, i + 1, combo)

ans = Solution()
print(ans.combine(4, 2))