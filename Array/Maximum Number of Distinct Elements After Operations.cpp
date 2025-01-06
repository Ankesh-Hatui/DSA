/*
* LeetCode : 3397
* LeetCode Contest : 429
* T.C : O(n)
* S.C : O(n)
*/
class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        int prev=INT_MIN;
        sort(nums.begin(),nums.end());
        int n=nums.size();
        set<int>set;
        for (int i=0;i<n;i++){
            int x=max(prev+1,nums[i]-k);

            if(x<=nums[i]+k){
                set.insert(x);
                prev=x;
            }
        }
        return set.size();
    }
};
