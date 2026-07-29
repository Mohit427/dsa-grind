class Solution(object):
    def judgeSquareSum(self, c):
        left=0
        right = int(c**0.5)+1
        while left<=right:
            res=left**2 + right**2
            if res == c:
                return True
            elif res<c:
                left+=1
            else:
                right-=1
        return False