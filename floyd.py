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

## Here we use the Floyd method mainly used to detect loops in linked list.
## So to do that, we first consider each value in nums as a pointer to an index. 
## then like in Floyd, we use the fast and slow pointer to tranverse the array
## the slow pointer moves one step at a time while the fast pointer moves two steps at a time.
## when the slow and the fast pointer meet the first time, that is not the solution
## after we find the first intersection point, we start the slow pointer again from the begginging and then move both slow and fast pointer one step at a time
## this is because, according to floyd, after the first point of intersection, the distance from the internsection point to the start of the loop (fast pointer) and
## the distance from the beginning to the start of the cycle(slow pointer) should be the same.

            
