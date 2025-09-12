class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == 'IV':
            return 4
        elif s == 'IX':
            return 9
        roman_digits = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500,
                        'M': 1000}
        roman_num = 0
        for i in range(len(s)):
            curr = roman_digits[s[i]]
            next_val = roman_digits[s[i + 1]] if i + 1 < len(s) else 0
            if curr < next_val:
                roman_num -= curr
            else:
                roman_num += curr
        return roman_num
        
        