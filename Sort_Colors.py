class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr=[0 for i in range(3)]
        for i in nums:
            arr[i]+=1
        val=0
        index=0
        for i in arr:
            while i:
                nums[index]=val
                i-=1
                index+=1
            val+=1