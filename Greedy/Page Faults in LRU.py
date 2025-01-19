'''
/*
* gfg
* T.C : O(N*C)
* S.C : O(N)
*/
'''
#User function Template for python3

class Solution:
    def pageFaults(self, N, C, pages):
        # code here
        q=[]
        freq=[False for _ in range(1001)]
        k=C
        fault=0
        for i in range(N):
            if freq[pages[i]]==False:
                if (k>0):
                    q.append(pages[i])
                    freq[pages[i]]=True
                    fault+=1
                    k-=1
                else:
                    removed=q.pop(0)
                    freq[removed]=False
                    q.append(pages[i])
                    #print(q)
                    fault+=1
                    freq[pages[i]]=True
            else:
                for j in range(len(q)):
                    if q[j]==pages[i]:
                        q.pop(j)
                        q.append(pages[i])
                        break
            
        return fault

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        pages = input().split()
        for itr in range(N):
            pages[itr] = int(pages[itr])
        C = int(input())

        ob = Solution()
        print(ob.pageFaults(N, C, pages))

# } Driver Code Ends