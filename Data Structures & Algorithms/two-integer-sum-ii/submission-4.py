class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        result=[]
        while l<r:
            sum = numbers[l]+numbers[r]
            if sum<target:
                l+=1
            elif sum>target:
                r-=1
            elif sum==target:
                result.extend([l+1,r+1])
                break
        return result
            