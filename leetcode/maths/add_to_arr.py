class Solution(object):
    def addToArrayForm(self, num, k):
        num_str = "".join(map(str, num))
        total = int(num_str) + k
        return list(map(int, str(total)))