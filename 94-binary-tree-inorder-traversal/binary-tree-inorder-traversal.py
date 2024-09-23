# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #we are gonna use recursive function because we want to get the leftmost node 
        #until there are no more lefts

        result = []

        def inOrderDFS(root):
            if not root:
                return 0

            inOrderDFS(root.left)
            #print(root)
            result.append(root.val)
            inOrderDFS(root.right)
            #print(root)

        inOrderDFS(root)
        return result 
            