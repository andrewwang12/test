class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

res = TreeNode()
root = [4,2,7,1,3]
val = 2
print(res.searchBST(root, val))
