class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0=0
        count1=0
        n=len(nums)
        for i in nums:
            if i==0:
                count0+=1
            elif i==1:
                count1+=1
        for i in range(0,count0):
            nums[i]=0
            print(nums)
        for i in range(count0,count0+count1):
            nums[i]=1
            print(nums)
        for i in range(count0+count1,n):
            nums[i]=2
            print(nums)
        
