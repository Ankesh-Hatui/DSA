/*
* Leetcode : 1930
* T.C : O(N^2logN)
* S.C : O(2N)
*/
class Solution {
    // void print(set<int>)
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<int,int>mp;
        vector<vector<int>>indices(256);
        for (int i=0;i<s.size();i++){
            mp[s[i]-'a']++;
            indices[s[i]-'a'].push_back(i);
        }
        int cnt=0;
        for (auto&ch:s){
            if (mp[ch-'a']>1){
                cout<<"character is: "<<(ch-'a')<<" "<<mp[ch-'a']<<"\n";
                int last_ind=indices[ch-'a'][indices[ch-'a'].size()-1];
                int first_ind=indices[ch-'a'][0];
                cout<<"li and fi: "<<last_ind<<" "<<first_ind<<"\n";
                string temp=s.substr(first_ind+1,last_ind-first_ind-1);
                cout<<temp<<"\n";
                set<char>st(temp.begin(),temp.end());
                // print(st);
                mp[ch-'a']=0;
                cnt+=st.size();
            }
        }
        return cnt;
    }
};
