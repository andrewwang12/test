class Solution:    
    def searchMatrix(self, matrix, target):
            if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
                return False
            
            m, n = len(matrix), len(matrix[0])
            start, end = 0, m*n-1
            while start <= end:
                mid = (start + end) // 2
                i, j = mid // 2, mid % 2
                if target > matrix[i][j]:
                    start = mid + 1
                elif target < matrix[i][j]:
                    end = mid - 1
                else:
                    return True
            return False
    
res = Solution()
m = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
t = 30
print(res.searchMatrix(m,t))















        