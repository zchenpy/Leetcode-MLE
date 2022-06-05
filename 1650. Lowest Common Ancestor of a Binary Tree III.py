1650. Lowest Common Ancestor of a Binary Tree III
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
  
class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        p_ancestor = {p,}
        while p:
            p_ancestor.add(p.parent)
            p=p.parent
            
        while q:
            if q in p_ancestor:
                return q
            q = q.parent
            
#Time complexity: O(2n)
#Space complexity:O(2n)            
