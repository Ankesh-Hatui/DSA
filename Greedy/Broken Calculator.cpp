/*
* Leetcode : 991
* T.C : O(log(target/sv))
* S.C : O(1)
*/
class Solution {
public:
    int brokenCalc(int sv, int target) {
        int cnt = 0;
        while (sv != target) {
            
            if (target>sv){
                if (target%2==0){
                    target/=2;
                }
                else{
                    target+=1;
                }
            }else{
                target+=1;
            }
            cnt++;
        }
        return cnt;
    }
};
