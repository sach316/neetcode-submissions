class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        count=[[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in hmap:
                hmap[i]=0
            hmap[i]+=1
        for i,j in hmap.items():
            count[j].append(i)
        result=[]
        for i in range(len(count)-1,0,-1):
            for j in count[i]:
                result.append(j)
                if len(result)==k:
                    return result