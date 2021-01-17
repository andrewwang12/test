class Solution:
    def subset(self, nums):
        res, subset = [], []
        self.backtrack(res, subset, nums, 0)
        return res

    def backtrack(self, res, subset, nums, i):
        if i == len(nums):
            res.append(subset.copy())
        else:
            self.backtrack(res, subset, nums, i + 1)
            subset.append(nums[i])
            self.backtrack(res, subset, nums, i + 1)
            subset.pop()

ans = Solution()
print(ans.subset([1,2,3]))

