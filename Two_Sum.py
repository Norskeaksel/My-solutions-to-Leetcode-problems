class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = {}
        for i in range(len(nums)):
            dick[nums[i]]=i
        for i in range(len(nums)):
            missing=target-nums[i]
            if missing in dick:
                if i!=dick[missing]:
                    return[i,dick[missing]]