class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_map = dict()
        for char in magazine:
            if char not in hash_map:
                hash_map[char] = 1
            else:
                hash_map[char] += 1
        
        for char in ransomNote:
            if char in hash_map and hash_map[char] > 0:
                hash_map[char] -= 1
            else:
                return False
        return True
        