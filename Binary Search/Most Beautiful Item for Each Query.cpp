/*
LeetCode : 2070
T.C : O(NlogN) + O(N)

S.C : O(1)

*/

class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        vector<int>ans;
        sort(items.begin(),items.end());
        int max_beauty=items[0][1];
        for (int i=1;i<items.size();i++){
            max_beauty=max(max_beauty,items[i][1]);
            items[i][1]=max_beauty;
        }

        for (int i=0;i<queries.size();i++){
            int l=0,r=items.size()-1;
            int res=0,beauty=0;

            while (l<=r){
                int mid=l+(r-l)/2;

                if (items[mid][0]<=queries[i]){
                    beauty=max(items[mid][1],beauty);
                    l=mid+1;
                }
                else{
                    r=mid-1;
                }
            }

            ans.push_back(beauty);
        }

        return ans;
    }
};
