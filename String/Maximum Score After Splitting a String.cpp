/*
* Leetcode : 1422
* T.C : O(N)
* S.C : O(1)
*/
class Solution {
public:
    int maxScore(string s) {
        int score=0;
        int zeros=0,ones=0;

        for (auto&it:s){
            if (it=='1'){
                ones+=1;
            }
        }

        for(int i=0;i<s.size()-1;i++){
            if (s[i]=='0'){
                zeros+=1;
            }
            else{
                ones-=1;
            }
            score=max(score,ones+zeros);
        }
        return score;
    }
};
