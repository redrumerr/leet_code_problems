class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in list(set(ransomNote)):
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True
        