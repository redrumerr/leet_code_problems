class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_digits = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 
                        'D': 500, 'M': 1000}
        roman_digits_spec = {'IV': 4, 'IX': 9, 'XL': 40, 
                            'XC': 90, 'CD': 400, 'CM': 900}
        roman_num = 0
        for key in roman_digits_spec:
            while key in s:
                roman_num += roman_digits_spec[key]
                s = s.replace(key, '', 1)
        for key in roman_digits:
            while key in s:
                roman_num += roman_digits[key]
                s = s.replace(key, '', 1)     
        return roman_num
        