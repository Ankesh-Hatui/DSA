/*
* Leetcode : 3223
* T.C : O(N)+O(26) N is the length of the string
* S.C : O(26)
*/

class Solution {
public:
    int minimumLength(string s) {
        vector<int>hash(26,0);
        for (auto&ch:s){
            hash[ch-'a']++;
        }
        int cnt=0;
        for(int&el:hash){
            if (el!=0 && el%2==0){
                cnt+=2;
            }
            else{
                cnt+=el%2;
            }
        }
        return cnt;
    }
};