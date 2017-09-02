'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

用栈实现
runtime 38ms

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c== '(':
                stack+= ')'
            elif c== '{':
                stack+= '}'
            elif c== '[':
                stack+= ']'
            elif stack== [] or stack.pop()!= c:
                return False
        return stack== []

#test
s = Solution()
string= '{'
print(s.isValid(string))
