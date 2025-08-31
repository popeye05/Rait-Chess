class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() #This is the set Constructor
        while(n!=1):
            sum1=0
            if n in seen:
                return False
            seen.add(n)
            while(n>0):
                digit = n%10
                sum1 += digit **2
                n /= 10
            n=sum1
        return True 

