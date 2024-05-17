//subsequences with sum k
#include<bits/stdc++.h>
using namespace std;

void solution(vector<int>a,vector<int>c,int k,int sum,int ind){
    if(ind>=a.size()){
        if(sum==k){
            for(auto i:c)cout<<i<<" ";
            cout<<endl;
        }
        
        return;
    }
    c.push_back(a[ind]);
    sum+=a[ind];
    solution(a,c,k,sum,ind+1);

    c.pop_back();
    sum-=a[ind];
    solution(a,c,k,sum,ind+1);
}

int main(){

    #ifndef ONLINE_JUDGE

        freopen("input.txt", "r", stdin);

        freopen("output.txt", "w", stdout);

    #endif // ONLINE_JUDGE

    int tc;
    cin>>tc;
    while(tc--){
        int n;
        cin>>n;
        vector<int>a(n,0);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        vector<int>c;
        int k;
        cin>>k;
        solution(a,c,k,0,0);
    }
}
