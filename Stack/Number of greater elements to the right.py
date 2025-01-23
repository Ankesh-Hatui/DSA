'''
* GFG
* T.C : O(N*queries)
* S.C : O(queries)
'''
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        # Code here
        ans=[]
        for el in indices:
            cnt=0
            for i in range(el+1,N):
                if arr[i]>arr[el]:
                    cnt+=1
            ans.append(cnt)
            
        return ans

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        queries = int(input())
        indices = list(map(int, input().split()))
        ob = Solution()
        NGEs = ob.count_NGEs(N, arr, queries, indices)
        for val in NGEs:
            print(val, end = ' ')
        print()
        print("~")
# } Driver Code Ends
