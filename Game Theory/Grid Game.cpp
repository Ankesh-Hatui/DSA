/*
* Leetcode : 2017
* T.C : O(N) N is no of cols
* S.C : 2*O(N)
*/
class Solution {
    typedef long long ll;
public:
    long long gridGame(vector<vector<int>>& grid) {
        vector<ll>rowsum1(grid[0].size(),0);
        vector<ll>rowsum2(grid[0].size(),0);

        for (int i=0;i<2;i++){
            rowsum1[0]=grid[0][0];
            rowsum2[0]=grid[1][0];
            for (int j=1;j<grid[i].size();j++){
                if (i==0){
                    rowsum1[j]=rowsum1[j-1]+grid[i][j];
                }
                else{
                    rowsum2[j]=rowsum2[j-1]+grid[i][j];
                }
            }
        }

        ll mini=LLONG_MAX;
        int n=grid[0].size();
        for (int i=0;i<n;i++){
            ll upper=rowsum1[n-1]-rowsum1[i];
            ll lower=rowsum2[i]-grid[1][i];

            if (upper==0 || lower==0){
                mini=min(mini,upper==0?lower:upper);
            }
            else{
                mini=min(mini,max(upper,lower));
            }

        }
        return mini;

    }
};
