class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        minus=""
        if s[0]=='-':
            minus="-"
            s=str(abs(x))
        revStr=minus
        for i in reversed(s):
            revStr+=i
        if abs(int(revStr))>2**31-1:
            return 0
        return int(revStr)