/*
* Lettcode : 2381
* T.C : O(N) max(N shifts queries size , size of string s)
* S.C : O(M) M size of string
* Reference : see video of codestorywithmik
*/

class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        int n = s.size();
        vector<int> diffArray(n, 0);

        for (auto& v : shifts) {

            int l = v[0];
            int r = v[1];
            int d = v[2];

            int x;

            if (d == 0) {
                x = -1;
            } else {
                x = 1;
            }

            diffArray[l] += x;
            if (r + 1 < n) {
                diffArray[r+1] -= x;
            }
        }

        // cummutative sum

        for (int i = 1; i < n; i++) {
            diffArray[i] = diffArray[i]+diffArray[i-1];
        }

        // wrap around

        for (int i=0;i<n;i++){
            int shift=diffArray[i]%26;

            if (shift<0){
                shift+=26;
            }
            s[i]=(((s[i]-'a')+shift)%26)+'a';
        }
        return s;
    }
};
