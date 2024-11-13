'''
LeetCode :
T.C : O(NlogN)
S.C : O(1)
'''

# Brute Force
for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                if (nums[i]+nums[j])>=lower and (nums[i]+nums[j])<=upper:
                    cnt+=1
        
        return cnt

# optimal Using BS

cnt=0
        nums.sort()

        for i in range(len(nums)):
            lw=bisect_left(nums,lower-nums[i],i+1)
            up=bisect_right(nums,upper-nums[i],i+1)

            cnt+=(up-lw)
        return cnt
