class Solution(object):
    def firstMatchingIndex(self, s):
        for i in range(len(s)//2+1):
            if s[i]==s[len(s)-i-1]:
                return i
        return -1