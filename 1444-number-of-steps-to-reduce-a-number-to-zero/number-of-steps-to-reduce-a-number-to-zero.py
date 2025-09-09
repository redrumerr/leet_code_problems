class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        counter = 0
        while num > 0:
            if not num & 1:
                num //= 2
            else:
                num -= 1
            counter += 1
        return counter
        