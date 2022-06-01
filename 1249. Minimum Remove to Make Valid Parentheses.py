1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        stack= []
       
        for e in s:
            if e.isalpha():
                stack.append(e)
            if e == '(':
                stack.append(e)
                count+=1
            if e == ')':
                if count >0:
                    stack.append(e)
                    count-=1
                else:
                    continue
                    
        if count == 0:
            return ''.join(stack)
        
        for i in range(len(stack)-1, -1, -1):
            if count == 0:
                break   
            if stack[i] =='(':
                stack[i] = ''
                count -= 1
        return ''.join(stack)    
        
        
#Time complexity: O(n)
#Space complexity:O(n)
