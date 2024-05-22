// subset of an array containing duplicate numbers
class Solution {
    void subset(vector<int>nums,vector<vector<int>>&ans,vector<int>curr,int ind){
        /*
        if(ind>=nums.size()){
            ans.insert(curr);
            return;
        }

        subset(nums,ans,curr,ind+1);

        curr.push_back(nums[ind]);
        subset(nums,ans,curr,ind+1);
        curr.pop_back();
        */

        // Better
        if(ind>=nums.size()){
            ans.push_back(curr);
            return;
        }

        curr.push_back(nums[ind]);
        subset(nums,ans,curr,ind+1);
        curr.pop_back();

        // To avoid duplicate numbers
        while(ind+1<nums.size() && nums[ind]==nums[ind+1]){
            ind++;
        }

        subset(nums,ans,curr,ind+1);
        
    }

public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {

        ios_base::sync_with_stdio(false);cin.tie(NULL);
        sort(nums.begin(),nums.end());
        vector<vector<int>>ans;
        vector<int>curr;
        subset(nums,ans,curr,0);
        // vector<vector<int>>res(ans.begin(),ans.end());
        return ans;
    }
};
