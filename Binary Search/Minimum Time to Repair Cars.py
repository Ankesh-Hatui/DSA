'''
* Leetcode : 2594
* T.C : O(NlogN)
* S.C : O(1)
'''

def isValid(nums,cars,time):
    cars_washed = 0
    n = len(nums)
    for i in range(n):
        cars_washed += math.floor((time//nums[i])**0.5)
    if (cars_washed<cars):
        return False
    return True


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        # As for minimising the time I need to use all mechanics
        max_el = max(ranks)
        left = 1
        right = max_el * (cars*cars)

        ans = float('inf')

        while left<=right:
            mid = left + (right - left)//2
            if (isValid(ranks,cars,mid)):
                ans = min(ans,mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans 
