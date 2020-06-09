def isSubsequence(s, t) -> bool:
    l=len(t)
    j = -1
    for v in (s):
        good = 0
        while j<l-1:
            j+=1
            if v == t[j]:
                good = 1
                break
        if good == 0:
            return False
    return True
s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))