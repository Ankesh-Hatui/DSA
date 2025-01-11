'''
* Leetcode : 3043
* T.C : O(N * K) N is size of max(Array1,2) K is max to max 8
* S.C : O(N*k) k size string or int for N size array 
'''

class Tree:
    def __init__(self):
        self.child=[None for _ in range(10)]
        self.end=False

def insert(root,s):
    curr=root
    for ch in s:
        digit=ord(ch)-ord('0')
        if (curr.child[digit]==None):
            curr.child[digit]=Tree()
        curr=curr.child[digit]
    curr.end=True
def search(root,s):
    curr=root
    cnt=0
    for ch in s:
        digit=ord(ch)-ord('0')
        if (curr.child[digit]==None):
            return cnt
        cnt+=1
        curr=curr.child[digit]
    return cnt
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root=Tree()
        for num in arr1:
            Num=str(num)
            insert(root,Num)
        
        maxi=0
        for num in arr2:
            Num=str(num)
            maxi=max(maxi,search(root,Num))
        return maxi