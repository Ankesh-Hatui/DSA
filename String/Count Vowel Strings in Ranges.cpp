/*
* Leetcode : 2559
* T.C: O(N)+O(M) here N is words length and M is queries length
* S.C : O(N)
*/
class Solution {
    bool isVowel(char ch) {
        string vowel = "aeiou";
        return vowel.find(ch) != string::npos;
    }

public:
    vector<int> vowelStrings(vector<string>& words,
                             vector<vector<int>>& queries) {

        int n = words.size();
        vector<int> vs(n, 0); // vowel strings
        int ind = 0;
        for (auto& str : words) {
            if (isVowel(str[0]) && isVowel(str[str.size() - 1])) {
                if (ind == 0) {
                    vs[ind] += 1;
                } else {
                    vs[ind] = vs[ind - 1] + 1;
                }

            } else {
                if (ind == 0) {
                    vs[ind] = 0;
                } else {
                    vs[ind] = vs[ind - 1];
                }
            }
            ind += 1;
        }

        vector<int> ans;
        for (auto& it : queries) {
            int l = it[0], r = it[1];
            if (l == 0) {
                ans.push_back(vs[r]);
            } else {
                ans.push_back(vs[r] - vs[l - 1]);
            }
        }
        return ans;
    }
};
