def ans(n,sec):
    if n==1:
        return sec
    string=""
    i=0
    while i<len(sec):
        c=1
        while i<len(sec)-1 and sec[i]==sec[i+1]:
            c+=1
            i+=1
        string+=str(c)+str(sec[i])
        i += 1
    return ans(n-1,string)

class Solution:
    def countAndSay(self, n: int) -> str:
        return ans(n,"1")
        