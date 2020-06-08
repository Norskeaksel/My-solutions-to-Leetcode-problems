class Solution:
    def firstUniqChar(self, s: str) -> int:
        keys=[]
        for i in s:
            keys.append(i)
        d=dict.fromkeys(keys,0)
        for i in s:
            d[i]+=1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1