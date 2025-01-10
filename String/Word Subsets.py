'''
* Leetcode : 916
* T.C : O(N)
* S.C : O(10)
'''
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_cnt=[0 for _ in range(26)]

        # Getting max count of every char of every str
        for st in words2:
            cnt=[0 for _ in range(26)]
            for ch in st:
                cnt[ord(ch)-ord('a')]+=1
                # print(cnt)
            for i in range(26):
                max_cnt[i]=max(max_cnt[i],cnt[i])

        # to store universal str
        ans=[]
        
        for st in words1:
            cnt=[0 for _ in range(26)]
            for ch in st:
                cnt[ord(ch)-ord('a')]+=1
            got_it=True
            for i in range(26):
                if (cnt[i]<max_cnt[i]):
                    got_it=False
                    break
            if (got_it):
                ans.append(st)
        
        return ans
