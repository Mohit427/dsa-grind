class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 aren't prime
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:  # if i is still marked as prime
                # mark all multiples of i as non-prime
                for j in range(i*i, n, i):  # start from i*i (earlier multiples already marked)
                    is_prime[j] = False
        
        return sum(is_prime)  # count remaining True values