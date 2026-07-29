class Solution(object):
    def countPairs(self, nums, target):
            nums.sort()
            left=0
            right=len(nums)-1
            ctr=0
            while(left<right):
                if nums[left]+nums[right]>=target:
                    right-=1
                
                else:
                    ctr+=(right-left)
                    left+=1
            return ctr

        