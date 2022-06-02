921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
  
#Stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        counter = 0
        step = 0
        for e in s:
            if e == '(':
                stack.append(e)
                counter+=1
            if e == ')':
                if stack:
                    stack.pop()
                    counter-=1
                else:
                    step +=1
        if counter == 0:
            return step  
        return counter+step
      
#Time complexity: O(n)
#Space complexity:O(n)     
