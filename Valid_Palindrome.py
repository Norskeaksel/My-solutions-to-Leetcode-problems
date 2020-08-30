class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        print(s)
        regex = re.compile('[^0-9a-z]')
        s=regex.sub('', s)
        print(s)
        l=len(s)
        for i in range(l//2):
            if s[i]!=s[l-1-i]:
                return False
        return True