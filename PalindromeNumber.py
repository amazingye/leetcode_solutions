'''
Determine whether an integer is a palindrome. Do this without extra space.
'''



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        isP=False
        s = str(x)
        if s[:]== s[::-1]:
                isP = True
        return isP

#test
s = Solution()
print(s.isPalindrome(2147447412))
