def isPrime(n):
    if n==2 or n==3:
        return 1
    if n<2 or n%2==0 or n%3==0:
        return 0
    for i in range(5,int(sqrt(n))+1,6):
        if n/(i)==n//(i) or n/(i+2)==n//(i+2):
            return 0
    return 1

class Solution:
    def countPrimes(self, n: int) -> int:
        ans=0
        for i in range(n):
            ans+=isPrime(i)
        return ans