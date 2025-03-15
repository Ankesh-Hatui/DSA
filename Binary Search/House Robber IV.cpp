/*
* Leetcode : 2560
* T.C : O(N*K)
* S.C : O(N*K)
*/
// DP Solution
// TLE 

class Solution {
    int solve(vector<int>&nums,int k ,int ind,vector<vector<int>>&dp){
        if (k<=0){
            return 0;
        }
        if (ind>=nums.size()){
            return INT_MAX;
        }

        if (dp[ind][k]!=-1){
            return dp[ind][k];
        }
        int take = 0,skip = INT_MAX;
        take = max(nums[ind],solve(nums,k-1,ind+2,dp));
        skip = solve(nums,k,ind+1,dp);
        
        return dp[ind][k] = min(take,skip);
    }
public:
    int minCapability(vector<int>& nums, int k) {
        vector<vector<int>>dp(nums.size(),vector<int>(k+1,-1));
        int ans = INT_MAX;
        for (int i=0;i<nums.size();i++){
            ans = min(ans,solve(nums,k,i,dp));
        }
        return ans;
    }
};
