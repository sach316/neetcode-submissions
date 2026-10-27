class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited=set()
        ans=0
        ptr=0
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[ptr])
                ptr+=1
            visited.add(s[i])
            ans=max(ans,i-ptr+1)
        return ans