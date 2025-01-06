/*
* LeetCode : 1578
* T.C : O(N)*O(M) N is size of string and M is maximum repeating char range
* S.C : O(1)
*/
class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int n=colors.size();
        int ans=0;
        int i=0;
        while (i<n){
            int j=i;
            while (j+1 < n && colors[j] == colors[j+1]){
                j++;
            }
            if (j>i){
                int maxi=0,total_cost=0;
                for (int k=i;k<=j;k++){
                    total_cost+=neededTime[k];
                    maxi=max(maxi,neededTime[k]);
                }
                // We only need minimum time so we left maximum one and take rest
                ans+=total_cost-maxi;
            }
            i=j+1;
        }
        return ans;
    }
};
