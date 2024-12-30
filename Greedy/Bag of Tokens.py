'''
* Leetcode : 948
* T.C : O(NlogN)
* S.C : O(1)
'''
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score=0
        maxi=0
        i,j=0,len(tokens)-1
        while (i<=j):
            if (power>=tokens[i]):
                score+=1
                power-=tokens[i]
                i+=1
            elif (score>=1):
                score-=1
                power+=tokens[j]
                j-=1
            else:
                break
            maxi=max(score,maxi)
        return maxi
