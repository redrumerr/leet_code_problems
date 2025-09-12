class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_digits = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500,
                        'M': 1000}
        roman_num = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_digits[s[i]] < roman_digits[s[i + 1]]:
                roman_num -= roman_digits[s[i]]
            else:
                roman_num += roman_digits[s[i]]
        return roman_num
        