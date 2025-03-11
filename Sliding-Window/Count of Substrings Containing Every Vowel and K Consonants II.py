'''
* Leetcode : 3306
* T.C : O(N)
* S.C : O(N)
'''
def isVowel(ch):
    return ch in 'aeiou'
def precompute(word):
    arr = [0]*len(word)
    last_ind_cons = len(word)
    for i in range(len(word)-1,-1,-1):
        arr [i] =last_ind_cons
        if not isVowel(word[i]):
            last_ind_cons = i
    return arr
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        i = 0
        j = 0
        n = len(word)

        arr = precompute(word)
        vowels = {}
        cons = 0
        result =0 
        while j < n:
            ch = word[j]

            if isVowel(ch):
                if vowels.get(ch ,0)==0:
                    vowels.setdefault(ch,1)
                else:
                    vowels[ch]+=1
            else:
                cons += 1
            
            while cons>k:
                ch = word[i]
                if isVowel(ch):
                    vowels[ch]-=1
                    if vowels[ch]==0:
                        vowels.pop(ch)
                else:
                    cons-=1
                i+=1
            while cons==k and len(vowels)==5 and i<n:
                result += arr[j]-j
                ch = word[i]
                if isVowel(ch):
                    vowels[ch]-=1
                    if vowels[ch]==0:
                        vowels.pop(ch)
                else:
                    cons -= 1
                i+=1
            j+=1
        return result
