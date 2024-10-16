# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # starting from the root -> O(n^2)
        # starting from the leaf -> O(n)
        res= 0
        def dfs(node):
            if not node:
                return 0
            nonlocal res

            maxLeft = dfs(node.left)             #2
            maxRight= dfs(node.right)            #1

            maxDiameter = maxLeft + maxRight     #3

            res = max(maxDiameter, res)          #max(3,0) =3
            return 1 + max(maxLeft, maxRight)    #1+2 =3            # gives the height of the current subtree
            

        dfs(root)
        return res
        

        



