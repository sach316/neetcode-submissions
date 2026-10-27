class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1={}
        count2={}
        for i in s1:
            count1[i]=1+count1.get(i,0)
        l=0
        r=0
        while r< len(s2):
            if s2[r] not in count1:
                l=r
                count2={}
                r+=1
                continue
            if r-l+1>len(s1):
                print(r,l)
                if s2[l] in count2:
                    count2[s2[l]]-=1
                l+=1
            count2[s2[r]]=1+count2.get(s2[r],0)
            print(count1,count2)
            r+=1
            if count2==count1:
                return True
        return False