class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.insert(0,1e9)
        bottoms=[]
        tops=[]
        for i in range(1,len(prices)-1):
            if prices[i]<=prices[i-1] and prices[i]<prices[i+1] and len(bottoms)-len(tops)==0:
                bottoms.append(i)
                print(prices[i])
            if prices[i]>=prices[i-1] and prices[i]>prices[i+1] and len(bottoms)>len(tops):
                tops.append(i)
        if len(bottoms)>len(tops):
            tops.append(len(prices)-1)
        profit=0
        l=min(len(bottoms),len(tops))
        for i in range(l):
            profit-=prices[bottoms[i]]
        for i in range(l):
            profit+=prices[tops[i]]
        return profit