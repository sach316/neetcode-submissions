class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""  
        count1={}
        count2={}
        l=0
        res,resLen=[-1,-1],float('infinity')
        
        for i in t:
            count1[i]=1+count1.get(i,0)
        have,need=0,len(count1)
        for r in range(len(s)): 
            count2[s[r]]=1+count2.get(s[r],0)
            if s[r] in count1 and count2[s[r]]==count1[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=r-l+1
                count2[s[l]]-=1     
                if s[l] in count1 and count2[s[l]]<count1[s[l]]:
                        have-=1
                l+=1
        l,r=res
        return s[l:r+1]
        