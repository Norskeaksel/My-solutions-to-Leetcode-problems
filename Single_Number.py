class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==1:
            return nums[0]
        if nums[1]!=nums[0]:
            return nums[0]
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                print(i)
                return nums[i]
        return nums[len(nums)-1]
            