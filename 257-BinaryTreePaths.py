class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root,"")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
            print(stack)
        return res
ans = Solution()
root = [1,2,3,"",5]
print(ans.binaryTreePaths(root))