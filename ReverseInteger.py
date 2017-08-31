'''

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

'''


class Solution(object):
    def reverse(self,x):
        while x%10 == 0 and x !=0:
            x = int(x/10)
        s = str(x)
        if s[0] == '-' or s[0] == '+':
            rs = s[0]
            a1 = s[1:]
            rs += a1[::-1]
        else:
            rs = s[::-1]

        if int(rs)<= 2147483647 and int(rs)>=-2147483648:
            return int(rs)
        else:
            return 0


#test
s = Solution()
print(s.reverse(1534236469))
