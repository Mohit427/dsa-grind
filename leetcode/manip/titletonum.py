class Solution(object):
    def titleToNumber(self, columnTitle):
        result = 0
        for char in columnTitle:
            digit = ord(char) - ord('A') + 1  # A=1, B=2, ..., Z=26
            result = result * 26 + digit
        return result