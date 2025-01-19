'''
/*
*GFG
* T.C : O(N)
* S.C : O(N)
*/
'''
# User function Template for Python3

class Solution:
    def leftSmaller(self, n, a):
        # code here
        # Circular Array technique
        n=len(a)
        stack=[]
        res=[-1 for _ in range(n)]
        for i in range(n):
            while stack and stack[-1]>=a[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]
            stack.append(a[i])
        return res

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
        print("~")
# } Driver Code Ends