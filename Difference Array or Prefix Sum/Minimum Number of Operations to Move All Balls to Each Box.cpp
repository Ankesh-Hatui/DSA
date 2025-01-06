/*
* Leetcode : 1769
* T.C : O(N)*O(M) N,M is size of string and no of total ones in the string
* S.C : O(M)
*/
class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int>ones;
        int n=boxes.size();
        for(int i=0;i<n;i++){
            if (boxes[i]=='1'){
                ones.push_back(i);
            }
        }
        vector<int>ans(n,0);
        for (int i=0;i<ones.size();i++){
            int j=0;
            while (j<boxes.size()){
                ans[j]+=abs(j-ones[i]);
                j++;
            }
        }
        return ans;
    }
};
