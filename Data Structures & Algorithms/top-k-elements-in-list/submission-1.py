class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resdic={}
        for i in nums:
            if i not in resdic:
                resdic[i]=0
            resdic[i]+=1
        result=sorted(resdic.items(),key= lambda x:x[1],reverse=True)
        resdic=dict(result)
        return list(resdic.keys())[:k]