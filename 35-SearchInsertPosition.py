class Solution:
    def searchInsertPosition(self, nums: 'List[int]', target: 'int') -> 'int':
        start, end = 0, len(nums) - 1
        mid = (start + end) // 2
        while start <= end:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) // 2
        return start

nums = [1,2,3,4,5,6,9,23]
target = 7
res = Solution()
print(res.searchInsertPosition(nums, target))