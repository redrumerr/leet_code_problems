class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        stack = []
        for e in s:
            if e in ['(', '{', '[']:
                stack.append(e)
            else:
                if stack:
                    if e == ')' and stack[-1] == '(':
                        stack.pop(-1)
                    elif e == ']' and stack[-1] == '[':
                        stack.pop(-1)
                    elif e == '}' and stack[-1] == '{':
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
        return not bool(stack)