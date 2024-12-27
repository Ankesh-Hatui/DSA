/*
* LeetCode : 1014
* T.C : O(N)
* S.C : O(1)
*/

class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        // Modified equation:
        /* 
        * (values[i]+i)+(values[j]-j)
        */
        int n=values.size();
        int prev_max=values[0];
        int ans=INT_MIN;
        for (int j=1;j<n;j++){
            // for (int i=j-1;i>=0;i--){
            //     ans=max(ans,values[i]+i + values[j]-j);
            // }
            ans=max(ans,values[j]-j+prev_max);
            prev_max=max(prev_max,values[j]+j);
        }
        return ans;
    }
};
