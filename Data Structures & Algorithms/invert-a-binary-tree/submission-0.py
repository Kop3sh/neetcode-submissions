# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        def dfs(i):
            if not i:
                return
            
            i.left, i.right = i.right, i.left
            dfs(i.left)
            dfs(i.right)
            return i
        
        return dfs(root)