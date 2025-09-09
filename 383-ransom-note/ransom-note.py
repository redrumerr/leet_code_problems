class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in range(len(magazine)):
            ransomNote = ransomNote.replace(magazine[i], '', 1)
            if not ransomNote:
                return True
        return False

        