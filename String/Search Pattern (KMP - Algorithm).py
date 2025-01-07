'''
* Coding Ninja: https://www.naukri.com/code360/problems/search-pattern-kmp-algorithm_8416386?interviewProblemRedirection=true&sort_entity=recents&sort_order=DESC&leftPanelTabValue=PROBLEM
* T.C : O(n*m)
* S.C : O(1)
'''
Brute Force:

from typing import List

def stringMatch(text: str, pattern: str) -> List[int]:
    # Write your code here.
    ans=[]
    for k in range(len(text)):
        i,j=k,0
        while (i<len(text) and j<len(pattern)):
            if (text[i]!=pattern[j]):
                break
            i+=1
            j+=1
        if (j==len(pattern)):
            ans.append(k+1)
    return ans
