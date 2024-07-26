class Solution {
public:
    int numberOfSubstrings(string s) {
        // Brute or Better

        /*
        int n = s.length();
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            unordered_map<char, int> mp;

            for (int j = i; j < n; j++) {
                mp[s[j]]++;
                if (mp.size() == 3) {
                    cnt=cnt+(n-j);
                    break;
                }
            }
        }

        return cnt;

        */


        // most optimal

        int lastseen_a=-1,lastseen_b=-1,lastseen_c=-1;
        int n=s.length(),cnt=0;

        for(int i=0;i<n;i++){
            if(s[i]=='a'){
                lastseen_a=i;
            }
            else if(s[i]=='b'){
                lastseen_b=i;
            }

            else if(s[i]=='c'){
                lastseen_c=i;
            }

            if(lastseen_a!=-1 && lastseen_b!=-1 && lastseen_c!=-1){
                int mini=min(lastseen_a,min(lastseen_b,lastseen_c));

                cnt=cnt+(mini+1);
            }
        }

        return cnt;
    }
};
