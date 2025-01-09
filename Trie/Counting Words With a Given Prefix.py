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
