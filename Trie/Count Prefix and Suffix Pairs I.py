'''
* Leetcode : 3042
* T.C : O(N*N)
* S.C : O(1)
* Brute Force
'''
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt=0
        for i in range(len(words)):
            m=len(words[i])
            for j in range(i+1,len(words)):

                n=len(words[j])
                if (len(words[j])<len(words[i])):
                    continue
                
                elif (words[j][0:m]==words[j][n-m:]==words[i]):
                    # print(words[j][0:m],words[j][n-m:])
                    # print()
                    cnt+=1
        return cnt
