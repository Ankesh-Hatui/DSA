'''
* Coding Ninja: https://www.naukri.com/code360/problems/count-distinct-substrings_985292?leftPanelTabValue=PROBLEM
* T.C : O(L^2) + O(L) # first for solve func and seond for insert function
* S.C : O(L) # For Trie
'''
class Tree:
    def __init__(self):
        self.child=[None for _ in range(26)]
        self.end=False

def insert(root,s):
    curr=root
    for ch in s:
        if curr.child[ord(ch)-ord('a')] is  None:
            curr.child[ord(ch)-ord('a')]=Tree()
        curr=curr.child[ord(ch)-ord('a')]
    curr.end=True
def solve(mySet,root):
    while not root.end:
        curr=root
        string=''
        k=-1
        while not curr.end:
            j=-1
            for i in range(26):
                if (curr.child[i]is not None):
                    string+=chr(ord('a')+i)
                    j=i
                    if k==-1:
                        k=i
                    break
            curr=curr.child[j]
            mySet.add(string)
            #print(string)
        root=root.child[k]
    return len(mySet)+1 # one for blank space
def countDistinctSubstrings(s):
    # Write your code here
    root=Tree()
    insert(root,s)
    mySet=set([])
    return solve(mySet,root)
