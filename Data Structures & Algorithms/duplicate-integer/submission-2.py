class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums=set()
        for i in nums:
            if i not in setnums:
                setnums.add(i)
            else:
                return True
        return False
        
        