class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        counter=0
        for i in nums:
            if i==0:
                counter+=1
        for i in range(counter):
            nums.remove(0)
            nums.append(0)
        return nums