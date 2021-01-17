class Solution:
    def searchMatrix(self, matrix, target):

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m, n = len(matrix), len(matrix[0])
        start, end = 0, n-1
        while start < m and end >= 0:
            if target == matrix[start][end]:
                return True
            elif target > matrix[start][end]:
                start +=  1
            else:
                end -= 1
        return False
res = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(res.searchMatrix(matrix, target))
