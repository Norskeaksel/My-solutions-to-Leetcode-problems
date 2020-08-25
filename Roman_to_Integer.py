class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000,
             '0': 0}
        s+='0'
        ans=0
        for i in range(len(s)-1):
            a=d[s[i]]
            b=d[s[i+1]]
            if a<b:
                ans-=a
            else:
                ans+=a
        return ans
