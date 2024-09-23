# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    

        #solution from up to down
        if not root:
            return

        temp = root.left 
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)      
        self.invertTree(root.right)            
        return root

        #solution from down to up
        # if not root:
        #     return

        # Left  = self.invertTree(root.left)     #1
        # Right = self.invertTree(root.right)    #3

        # root.left, root.right = Right, Left
 

        # return root
        



        invertBinaryTree(root)
        return root

       

        
        return root
        