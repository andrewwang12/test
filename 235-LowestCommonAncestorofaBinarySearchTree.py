class TreeNode:
    def __init__(self, x):
        self.val = val 
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root.val == p or root.val == q:
            return root
        if p.val < root.val < q.val or p.val > root.val > q.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left)
        else:
            return self.lowestCommonAncestor(root.right)
