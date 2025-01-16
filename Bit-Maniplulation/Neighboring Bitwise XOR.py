'''
/*
* Leetcode : 2583
* T.C : O(N)+O(N)
* S.C : O(N)
*/
'''
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n=len(derived)
        original=[0 for _ in range(len(derived))]
        for i in range(1,len(derived)):
            original[i]=original[i-1]^derived[i]
        print(original)
        if original[0]^original[n-1]==derived[0]:
            return True
        original[0]=1
        for i in range(1,n):
            original[i]=original[i-1]^derived[i]

        if original[0]^original[n-1]==derived[0]:
            return True
        return False

