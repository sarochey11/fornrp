class Solution(object):
    def romanToInt(self, s):
        romanMap = {
            "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000
        }
        outPut = 0
        
        for i in range(len(s)):
            if i > 0 and romanMap[s[i]] > romanMap[s[i - 1]]:
                outPut += romanMap[s[i]] - 2 * romanMap[s[i - 1]]
            else:
                outPut += romanMap[s[i]]
        
        return (outPut)