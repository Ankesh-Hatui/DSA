/*
// Leetcode : 3011
// Time Complexiety: O(N)
// space Comlexity:O(M) (M is array can be broken into no of smaller seg)
*/

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bits=[]
        seg=[]
        n=len(nums)
        ans=True
        prev=0
        for el in nums:
            bit=bin(el).count('1')
            #print(bit)
            if len(bits)==0 or prev==bit:
                bits.append(el)
                prev=bit
                #print(bits)
            else:
                print(bits)
                seg.append(bits[:])
                bits.clear()
                prev=bit
                bits.append(el)
        if bits:
            seg.append(bits[:])
        print(seg)
        for i in range(1,len(seg)):
            maxi=max(seg[i-1])
            mini=min(seg[i])

            if maxi>mini:

                return False
        return True
