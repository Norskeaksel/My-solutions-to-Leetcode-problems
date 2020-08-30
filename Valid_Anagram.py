class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        keys=[]
        for i in s:
            keys.append(i)
        for i in t:
            keys.append(i)
        a=dict.fromkeys(keys,0)
        for i in s:
            a[i]+=1
        for i in t:
            keys.append(i)
        b=dict.fromkeys(keys,0)
        for i in t:
            b[i]+=1
        for i in range(len(s)):
            if a[s[i]]!=b[s[i]]:
                return False
        return True