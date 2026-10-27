class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l=0
        for r in range(k-1,len(nums)):
            print(nums[l:r+1],max(nums[l:r+1]))
            maxnum=max(nums[l:r+1])
            l+=1
            res.append(maxnum)
        return res