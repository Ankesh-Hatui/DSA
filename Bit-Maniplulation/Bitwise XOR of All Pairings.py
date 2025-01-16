'''
/*
* Leetcode : 2425
* T.C : O(N) N size of Array
* S.C : O(1)
*/
'''
class Solution:
    def xorAllNums(self, a1: List[int], a2: List[int]) -> int:
        xor_odd=-1
        arr1,arr2=False,False

        if len(a1)%2!=0:
            xor_odd=0
            arr1=True
            for el in (a1):
                xor_odd^=el
        
        if len(a2)%2!=0:
            # xor_odd=0
            if (xor_odd==-1):
                xor_odd=0
            arr2=True
            for el in a2:
                xor_odd^=el
        if xor_odd==-1:
            print(0)
            return 0
    
        if arr1 and arr2:
            print(xor_odd)
            return xor_odd
    
        ans=0    
        if arr1:
            for el in a2:
                ans^=el
        else:
            for el in a1:
                ans^=el
        # print(ans)
        return ans