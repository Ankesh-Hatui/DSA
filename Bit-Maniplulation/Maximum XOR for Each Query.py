#LeetCode:1829
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_sum=[0 for i in range(len(nums))]
        prefix_sum[0]=nums[0]
        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1]^nums[i]


        q=len(nums)-1
        RET=[]
        for el in prefix_sum:
            # maximum xor of any el is 2^maximumBit-1 in the range of 2^maximumBit
            max_xor=el ^ ((1<<maximumBit)-1)
            RET.append(max_xor)
        RET=list(reversed(RET))
        return RET
