class Solution(object):
    def canJump(self, nums):
        target = len(nums) - 1    # start with the end as the target
        for i in range(len(nums) - 2, -1, -1):   # walk backwards from second-to-last
            if i + nums[i] >= target:            # can this position reach the target?
                target = i                        # yes, so now reaching THIS position is enough
        return target == 0                        # did we shrink target all the way to start?
        
        