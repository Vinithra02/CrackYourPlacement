class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited=[]
        for i in range(len(nums)):
            if nums[i] in visited:
                nums[i]=101
            else:
                visited.append(nums[i])
        nums.sort()
        return len(visited)
        
