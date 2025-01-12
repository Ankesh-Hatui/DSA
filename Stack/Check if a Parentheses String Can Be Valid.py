'''
* Leetcode : 2116
* T.C : O(N)
* S.C : O(N)
'''
# Brute Force
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack=[]
        n=len(s)
        openClose=[]
        for i in range(len(s)):
            if (locked[i]=='0'):
                openClose.append(i)
            else:
                if (s[i]==')' and len(stack)!=0):
                    stack.pop()
                elif(s[i]==')' and len(openClose)!=0):
                    openClose.pop()
                elif (s[i]==')'):
                    return False
                else:
                    stack.append(i)

        i=len(openClose)-1
        m=len(stack)
        if (len(stack)>len(openClose)):
            return False
        for j in range(m-1,-1,-1):
            if (stack[j]>openClose[-1]):
                return False
            else:
                openClose.pop()
        if (len(openClose)!=0):
            if (len(openClose)%2==0):
                return True
            else:
                return False
        return True
                