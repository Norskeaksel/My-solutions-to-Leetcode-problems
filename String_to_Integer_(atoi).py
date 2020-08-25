import re
class Solution:
    def myAtoi(self, str: str) -> int:
        findNum = re.compile(r" *[\+-]?\d+")
        found = findNum.search(str)
        if found == None or found.start() != 0:
            return 0
            
        num = int(found.group())
        return min(max(num, -2 ** 31), 2 ** 31-1)