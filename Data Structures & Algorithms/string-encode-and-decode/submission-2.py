class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter="#"
        result=''
        for i in strs:
            result+=str(len(i))+delimiter+i
        return result
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        delimiter="#"
        while i<len(s):
            j=i
            while s[j]!=delimiter:
                j+=1
            length=int(s[i:j])
            result.append(s[j+1:j+length+1])
            i=j+length+1
        return result