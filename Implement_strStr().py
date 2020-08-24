class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        find=re.compile(needle)
        found=find.search(haystack)
        if found==None:
            return -1
        else:
            return found.start()