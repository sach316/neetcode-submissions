class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char=dict()
        if len(s)!= len(t):
            return False
        for i in s:
            if i not in char:
                char[i]=1
            else:
                char[i]+=1
        for i in t:
            if i in char:
                char[i]-=1
        for i in char.values():
            print(char.values(),i)
            if i >0:
                return False

        return True