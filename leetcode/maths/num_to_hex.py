class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        # Convert to 32-bit representation (handles negatives)
        num = num & 0xffffffff
        
        while num:
            remainder = num % 16
            result = hex_chars[remainder] + result  # prepend the hex digit
            num //= 16
        
        return result