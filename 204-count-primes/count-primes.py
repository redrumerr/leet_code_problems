class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        nums = [True] * n
        nums[0] = nums[1] = False
        for i in range(2, n):
            if nums[i]:
                j = 2 * i
                while j < n:
                    nums[j] = False
                    j += i
            i += 1
        return sum(nums)
        