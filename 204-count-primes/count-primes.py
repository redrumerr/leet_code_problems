class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        nums = [1] * n
        nums[0] = nums[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if nums[i]:
                for j in range(i * i, n, i):
                    nums[j] = 0
            i += 1
        return sum(nums)
        