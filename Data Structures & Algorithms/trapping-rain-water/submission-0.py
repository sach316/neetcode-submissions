class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        area=0
        leftMax,rightMax=height[l],height[r]
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax,height[l])
                area+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax,height[r])
                area+=rightMax-height[r]
        return area