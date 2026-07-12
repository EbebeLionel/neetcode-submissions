# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        def dfs(node):
            if not node:
                return []

            left = dfs(node.left)
            right = dfs(node.right)

            return left + [node.val] + right

        array = dfs(root)

        return array[k - 1]
        '''

        self.count = k
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return 

            inorder(node.left)

            self.count -= 1
            if self.count == 0:
                self.result = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.result