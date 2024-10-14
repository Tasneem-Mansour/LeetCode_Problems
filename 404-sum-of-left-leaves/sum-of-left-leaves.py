# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root or (not root.left and not root.right):
            return 0
        #BFS
        # q = deque([root])
        # sum = 0
        # while q:        
        #     node = q.popleft()         
        #     if node:
        #         if node.left and not node.left.left and not node.left.right:
        #             sum += node.left.val
                
        #         q.append(node.left)
        #         q.append(node.right)
        # return sum        

        #DFS
        self.sum = 0
        def dfs(node):
            if node:    
                if node.left and not node.left.left and not node.left.right:
                    self.sum += node.left.val  #9+15
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.sum
         
        