'''
* Leetcode : 1408
* T.C : O(n^2∗k) where n is number of words and k is average word length
* S.C : O(m) where m is number of matching substrings found
'''

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            string1=words[i]

            for j in range(len(words)):
                if (string1 in words[j] and string1!=words[j]):
                    ans.append(string1)
                    break
        return ans
