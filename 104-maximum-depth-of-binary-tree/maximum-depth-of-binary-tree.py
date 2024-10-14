# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #BFS
        # q = deque([root])
        # level = 0
        # while q:        #9 20
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        #Recursive DFS - Inorder - left, node, right  O(n)
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #Iterative DFS - preorder - node, left, right
        stack = [[root, 1]]     #[, [20,2], [9,2]]
        res = 0
        while stack:
            node, level = stack.pop()
            # res = max(res, level)
            # if node.right:
            #     stack.append([node.right, level+1])
            # if node.left:
            #     stack.append([node.left, level+1])

            if node:        #node can ne null as its children will be added even if null
                res = max(res, level)
                stack.append([node.right, level+1])
                stack.append([node.left, level+1])

        return res
        