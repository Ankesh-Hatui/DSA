/*
LeetCode: 2064

T.C: NlogN
S.C : O(1)

*/

class Solution {

    bool fesiable(int mid,vector<int>&q,int n){
        for (int el:q){
            n-=(el+mid-1)/mid;

            if (n<0){
                return false;
            }
        }

        return true;
    }
    
public:
    int minimizedMaximum(int n, vector<int>& q) {
        int left=1;
        int right=*max_element(q.begin(),q.end());
        int ans=0;

        while(left<=right){
            int mid=left+(right-left)/2;

            if (fesiable(mid,q,n)){
                ans=mid;
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }

        return ans;
    }
};
