class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for i in bills:
            if i==5:
                five +=1
            elif i==10 and five > 0:
                five-=1
                ten+=1
            elif i==20:
                if five>0 and ten >0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
            else:
                return False
        return True

        
