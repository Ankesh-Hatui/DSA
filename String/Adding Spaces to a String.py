"""
LeetCode - 2109
T.C : O(N)
S.C : O(N)
"""
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        """
        k=0
        for el in spaces:
            el+=k
            str_left=s[:el]
            str_right=s[el:]
            k+=1
            s=str_left+' '+str_right
        
        return s
        """
        """
        li=list(s)
        #spaces.sort(reverse=True)
        for i  in spaces[::-1]:

            li.insert(i,' ')
        ans=''.join(li)
        return ans
        """

        ans=[]
        space_ind=0

        for i in range(len(s)):
            if space_ind<len(spaces) and spaces[space_ind]==i:
                ans.append(' ')
                space_ind+=1
            ans.append(s[i])
        string =''.join(ans)
        return string
