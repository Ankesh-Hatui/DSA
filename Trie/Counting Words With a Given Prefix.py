'''
* Leetcode : 2185
* T.C : O(N)
* S.C : O(1)
* Brute Force
'''
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        m=len(pref)
        cnt=0
        for i in range(len(words)):
            pref_str=words[i][:m]
            if pref_str==pref:
                cnt+=1
        return cnt
----------------------------------------------------------------------------------------------------------------------------------------------------
'''
* T.C: O(N*L) where L is length of the word and N is the no of words
* S.C : O(N*L) for every N words stored and L is the length of that word
* using Tries Solution
'''
class Tree{
    public:
    Tree *child[26];
    bool end=false;
    int cnt=0;
    Tree(){
        this->end=false;
        for (int i=0;i<26;i++){
            this->child[i]=nullptr;
        }
        this->cnt=0;
    }
};
void insert(Tree*root,string s){
    Tree *curr=root;
    for (auto&ch:s){
        if (curr->child[ch-'a']==nullptr){
            curr->child[ch-'a']=new Tree();
        }
        
        curr=curr->child[ch-'a'];
        curr->cnt+=1;
    }
    curr->end=true;
}
int search(Tree*root,string s){
    Tree *curr=root;
    int count=0;
    for (auto&ch:s){
        if (curr->child[ch-'a']==nullptr){
            return 0;
        }
        
        curr=curr->child[ch-'a'];
        
    }
    return curr->cnt;
}
class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        Tree*root=new Tree();
        for (auto&str:words){
            insert(root,str);
        }
        return search(root,pref);
    }
};
