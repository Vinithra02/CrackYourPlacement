class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        slow=nums[0]
        fast=nums[0]
        while(1):
                slow=nums[slow]
                fast=nums[nums[fast]]
                if slow==fast:
                    break
        slow=nums[0]
        while(slow!=fast):
            slow=nums[slow]
            fast=nums[fast]
        return slow
                    

            
