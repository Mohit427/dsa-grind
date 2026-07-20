class Solution(object):
    def jump(self, nums):
        jumps=0
        current_max=0
        next_max=0

        for i in range(len(nums)-1):
            next_max=max(next_max,nums[i]+i)

            if i==current_max:
                jumps+=1
                current_max=next_max
        return jumps        