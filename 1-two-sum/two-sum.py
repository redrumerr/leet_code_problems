class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 2 and sum(nums) == target:
            return [i for i in range(len(nums))]

        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i

        for i in range(len(nums)):
            x = target - nums[i]
            if nums.count(x) <= 0:
                continue
            else:
                if x in hash_map and i != hash_map[x]:
                    return [i, hash_map[x]]
            
        