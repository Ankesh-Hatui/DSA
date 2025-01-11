'''
* Leetcode : 1400
* T.C : O(N) + O(26) N is the size of string
* S.C : O(26) size of freq Array
'''
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq=[0 for _ in range(26)]

        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        no_even,no_odd=0,0
        if (len(s)==k):
            return True
        if (len(s)<k):
            return False
        for el in freq:
            if (el%2==0):
                no_even+=(el//2)
            else:
                no_even+=el//2
                no_odd+=1
        if (no_odd>k):
            return False
        return True