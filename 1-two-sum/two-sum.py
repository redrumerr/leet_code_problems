class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index, num in enumerate(nums):
            if target - num in hash_map:
                return [index, hash_map[target - num]]
            hash_map[num] = index
        