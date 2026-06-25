class Solution(object):
    def maxSubArray(self, nums):
        current=nums[0]
        best=nums[0]
        for i in range(1,len(nums)):
            current=max(current+nums[i],nums[i])
            best=max(current, best)
        return best

        