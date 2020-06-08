class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        comb=nums1+nums2
        dick1={}
        dick2={}
        for i in comb:
            dick1[i]=0
            dick2[i]=0
        for i in nums1:
            dick1[i]+=1
        for i in nums2:
            dick2[i]+=1
        ans=[]
        for i in dick1:
            m=min(dick1[i],dick2[i])
            for j in range(m):
                ans.append(i)
        return ans