//Susequences through recursion
/*
1. first take or not take
2.always second recursion call execute after first recursion complete
3.auxiliary space means how much stack space use let if there is 3 length array for
this case space o(n);
*/
#include<bits/stdc++.h>
using namespace std;

void printSequences(vector<int>c,int ind,vector<int>a){
    if(ind>=a.size()){
        if(c.size()==0){
            cout<<"{}";
        }
        for(auto i:c){
            cout<<i<<" ";
        }
        cout<<endl;
        return;
    }

    // if you want to not take first
    printSequences(c,ind+1,a);
    c.push_back(a[ind]);
    printSequences(c,ind+1,a);

    c.pop_back();
    // if you want to take first then not take 
    //printSequences(c,ind+1,a);
}

int main(){

    #ifndef ONLINE_JUDGE

        freopen("input.txt", "r", stdin);

        freopen("output.txt", "w", stdout);

    #endif // ONLINE_JUDGE

    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int>a(n,0);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        vector<int>c;
        printSequences(c,0,a);
        cout<<"for"<<t<<" th"<<" case "<<endl;
    }
}
