class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return []
            
            left = dfs(node.left)
            right = dfs(node.right)

            return left + [node.val] + right

        return dfs(root)