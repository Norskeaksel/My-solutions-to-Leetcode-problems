class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strarr=[str(i) for i in digits]
        print(strarr)
        str1=""
        for i in strarr:
            str1+=i 
        print(str1)
        num = int(str1)
        num+=1
        newstr=str(num)
        print(newstr)
        ans=[]
        for i in newstr:
            ans.append(i)
        return ans