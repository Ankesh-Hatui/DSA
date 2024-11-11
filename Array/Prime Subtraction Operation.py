"""
  LeetCode: 2601
  T.c : O(N) # without sieve
  T.C : log log (1001)
  S.C : O(1001)
  # for Prime Number
"""

class Solution:
    def getPrime(self,prime):
        for i in range(2,1001):
            if (i*i>1001):
                break
            if prime[i]:
                for j in range(i*i,1001,i):
                    prime[j]=False
    
    def primeSubOperation(self, nums: List[int]) -> bool:
        # store the prime number

        prime=[True for i in range(1001)]

        self.getPrime(prime)
        n=len(nums)
        
        for i in range(n-2,-1,-1):

            if nums[i]<nums[i+1]:
                continue

            for j in range(2,nums[i]):
                if prime[j] and nums[i]-j<nums[i+1]:
                    nums[i]-=j
                    break
                
            if nums[i]>=nums[i+1]:
                return False
        
        return True
