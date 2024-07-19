class Solution:

    def findMinDiff(self, A,N,M):
        
        # code here
        A.sort()
        curr=1000000
        for i in range(0,N-M+1):
            maximum=A[i+M-1]
            minimum=A[i]
            diff=maximum-minimum
            if diff<curr:
                curr=diff
        return curr
