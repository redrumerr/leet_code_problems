class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev_num = 0
        num = x
        while num > 0:
            rev_num = rev_num * 10 + num % 10
            num //= 10
        return rev_num == x