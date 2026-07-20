class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        
        sum_divisors = 1  # 1 is always a divisor
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                sum_divisors += i
                if i != num // i:  # avoid double-counting for perfect squares
                    sum_divisors += num // i
        
        return sum_divisors == num