'''
U, key = 3
          5     <
        /  \
       3    9   
      / \
     1   4


M
-Tree Problem
P
-while current is not None
    -if key is less than current.val
        -if current.left.val is equal to key:
            -store current.left.right in temporary variable
            -Set current.left to current.left.left
            -set current.left.right to temporary variable
            -return root

        -else:
            -current = current.left

    -elif key is greater than current.val:
        -if current.right.val is equal to key:
            -store current.right.left in temporary variable
            -set current.right to current.right.right
            -if current.right.val > temp.val:
                -current.right.left equal to temp
                -return root
            -else:
                -current.right.right equal to temp
                -return root
        -else:
            -current = current.right
IRE
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Step 1: Find the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # Step 2: We found the node! Handle deletion cases
        else:
            # Case 1 & 2: No children, or only 1 child (Right child exists or both None)
            if not root.left:
                return root.right
            # Case 2: Only 1 child (Left child exists)
            elif not root.right:
                return root.left
            
            # Case 3: Node has TWO children
            # Find the min value node in the right subtree (Inorder Successor)
            successor = root.right
            while successor.left:
                successor = successor.left
                
            # Replace current node's value with successor's value
            root.val = successor.val
            
            # Delete the duplicate successor from the right subtree
            root.right = self.deleteNode(root.right, successor.val)
            
        return root

