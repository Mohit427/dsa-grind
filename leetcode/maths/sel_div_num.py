class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []
        for num in range(left, right + 1):
            # skip if contains 0 (fast string check)
            if '0' not in str(num):
                # short-circuit: stops as soon as a digit doesn't divide num
                if all(num % int(digit) == 0 for digit in str(num)):
                    result.append(num)
        return result