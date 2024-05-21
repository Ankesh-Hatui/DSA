class Solution {
    void combination(vector<int>candidates,vector<vector<int>>&ans,vector<int>curr,int target,int ind){
        
        if(target==0){
            ans.push_back(curr);
            return;
        }

        for(int i=ind;i<candidates.size();i++){
            
            // if there are multiple same value we will skip
            if(i>ind && candidates[i]==candidates[i-1]){
                continue;
            }

            // if we get a value is more than our target we can either return or break;
            if(candidates[i]>target){
                // break;
                return;
            }
            curr.push_back(candidates[i]);
            combination(candidates,ans,curr,target-candidates[i],i+1);

            // backtrack
            curr.pop_back();
        }

    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        vector<vector<int>>ans;
        vector<int>curr;
        // must sort original given array
        sort(candidates.begin(),candidates.end());
        combination(candidates,ans,curr,target,0);
        return ans;
    }
};
