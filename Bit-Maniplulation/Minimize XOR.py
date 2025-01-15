'''
* Leetcode : 2429
* T.C : O(1)
* S.C : O(1)
'''

class Solution:
    def getMSB(self,n):
        n|=n>>1
        n|=n>>2
        n|=n>>4
        n|=n>>8
        n|=n>>16
        n+=1
        return n>>1
    def minimizeXor(self, num1: int, num2: int) -> int:
        ones_num1=bin(num1).count('1')
        ones_num2=bin(num2).count('1')
        ans=num1
        if ones_num1==ones_num2:
            return num1
        elif ones_num1>ones_num2:
            num=self.getMSB(num1)
            ans=num
            print(ans)
            while num!=0:
                if num & num1!=0:
                    ans|=num
                    ones_num2-=1
                num=num>>1
                if ones_num2==0:
                    break
        else:
            ones_num2-=ones_num1
            for i in range(0,31):
                if (1<<i)&num1==0:
                    ans|=(1<<i)
                    ones_num2-=1
                if (ones_num2==0):
                    break
        return ans
