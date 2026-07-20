class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        result = ""
        
        while num:
            remainder = num % 7
            result = str(remainder) + result  # prepend the digit
            num //= 7
        
        return ("-" if negative else "") + result