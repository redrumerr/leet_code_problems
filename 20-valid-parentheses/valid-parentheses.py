class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        map_ = {')': '(', '}': '{', ']': '['}
        stack = []
        for e in s:
            if e in map_.values():
                stack.append(e)
            else:
                if not stack or map_[e] != stack.pop():
                    return False
        return not stack