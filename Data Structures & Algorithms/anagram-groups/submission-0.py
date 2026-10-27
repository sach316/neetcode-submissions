class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=dict()
        for i in strs:
            count=[0]*26

            for j in i:
                count[ord(j)-ord('a')]+=1
            key=tuple(count)
            if key not in result:
                result[key]=[i]
            else:
                result[tuple(count)].append(i)
        return result.values()