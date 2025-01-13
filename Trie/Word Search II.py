'''
* Leetcode : 212
* T.C : O(M*N)
* S.C : O(M * N)
'''
class Tree:
    def __init__(self):
        self.child=[None for _ in range(26)]
        self.end=False
        self.word=""
def insert(root,word):
    curr=root
    for ch in word:
        if (curr.child[ord(ch)-ord('a')]==None):
            curr.child[ord(ch)-ord('a')]=Tree()
        curr=curr.child[ord(ch)-ord('a')]
    curr.end=True
    curr.word=word
def search(mat,root,visited,r,c,ans,Dir):
    visited[r][c]=True
    ch=mat[r][c]
    if (root.child[ord(ch)-ord('a')]is not None):
        if (root.child[ord(ch)-ord('a')].end==True):
            ans.append(root.child[ord(ch)-ord('a')].word)
            root.child[ord(ch)-ord('a')].end=False
        for i in range(4):
            newR=r+Dir[i][0]
            newC=c+Dir[i][1]
            if (newR<len(mat) and newR>=0 and newC<len(mat[0]) and newC>=0 and not visited[newR][newC]):
            
                search(mat,root.child[ord(ch)-ord('a')],visited,newR,newC,ans,Dir)
    visited[r][c]=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Tree()
        for word in words:
            insert(root,word)
        Dir=[[1,0],[0,-1],[0,1],[-1,0]]
        visited=[[False for _ in range(len(board[0]))] for _ in range(len(board))]
        ans=[]
        for i in range(len(board)):
            for j in range(len(board[i])):
                search(board,root,visited,i,j,ans,Dir)
        return ans