236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents_dic = {root:None}  
        def parents(root):
            if not root:
                return
            if root.left:
                parents_dic[root.left] = root
            if root.right:
                parents_dic[root.right] = root
            #print(self.ancestor(root.left) and self.ancestor(root.right))
            parents(root.left)
            parents(root.right)
        
        parents(root)  

        p_ancestor = set()
        while p:
            p_ancestor.add(p)
            p = parents_dic[p]
            
        while q:
            if q in p_ancestor:
                return q
            q = parents_dic[q]
            
#Time complexity: O(n)
#Space complexity:O(n)                
