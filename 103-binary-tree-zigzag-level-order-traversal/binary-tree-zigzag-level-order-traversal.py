# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        q = deque([root])
        level = 0
        res = []
        while q:            
            dummy = []
            for i in range(0, len(q)):
                node = q.popleft()   
                dummy.append(node.val)   
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(dummy)
        for i in range(len(res)):
            if i%2 != 0:
                res[i].reverse()

        print(res)
        return res