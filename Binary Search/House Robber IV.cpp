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





// Optimal Solution

// Binary Search
// T.C : O(NlogM) , where M is maximum possible capability
// S.C : O(1)

class Solution {
    bool isValid(vector<int>&nums,int num,int k){
        int cnt = 0;
        for (int i=0;i<nums.size();){
            if (nums[i]<=num){
                cnt += 1;
                i+=2;
            }
            else{
                i+=1;
            }
        }
        if (cnt>=k){
            return true;
        }
        return false;
    }
public:
    int minCapability(vector<int>& nums, int k) {
        int left = *min_element(nums.begin(),nums.end());
        int right = *max_element(nums.begin(),nums.end());

        int ans = 0;

        while (left<=right){
            int mid = left + (right-left)/2;
            if (isValid(nums,mid,k)){
                ans = mid;
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }
        return ans ;
    }
};
