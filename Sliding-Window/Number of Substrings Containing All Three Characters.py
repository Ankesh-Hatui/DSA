'''
* Leetcode : 1356
* T.C : O(N)
* S.C : O(1) # a dictionary of size 3 still constant
'''

def valid(ch):
    return ch in 'abc'
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i,j = 0,0
        d = {}
        cnt = 0
        n = len(s)
        while j<n:
            if valid(s[j]):
                if d.get(s[j],0)==0:
                    d.setdefault(s[j],1)
                else:
                    d[s[j]]+=1
            while len(d)==3:
                cnt += n - j
                if valid(s[i]):
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        d.pop(s[i])
                i+=1
            j+=1
        return cnt


'''
NOTE : 

**Most Important Part of this Question While solving with Sliding Window**

1 . Count answer len(s) - j where j is current position

beacuse here see 
ex : "abcabc"

if you get a valid substring as 'abc' then after that as many char present still this string will be valid so , remaing char is n - j after j th char in the string 
'''
