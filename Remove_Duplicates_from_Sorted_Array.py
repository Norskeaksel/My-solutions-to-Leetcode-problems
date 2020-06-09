class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        i=0
        while(i<l):
            i+=1
            #print(nums,l,i)
            if l>1 and i>=1 and i<l:
                if nums[i]==nums[i-1]:
                    nums.remove(nums[i-1])
                    i-=2
                    l-=1
        return len(nums)