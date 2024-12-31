'''
* Leetcode : 881
* href: https://leetcode.com/problems/boats-to-save-people/description/
* T.C : O(N)
* S.C : O(N)
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        false=1
        true=0
        i=0
        cnt=0
        n=len(people)
        visited=[false for _ in range(len(people))]
        j=n-1
        while (i<len(people)):
            
            if (visited[i]==true):
                cnt+=sum(visited)
                break
            get=false
            while (i<j):
                if (people[i]+people[j]<=limit and visited[j]==false):
                    visited[j]=true
                    cnt+=1
                    get=true
                    break
                j-=1
            if (get==false):
                cnt+=1
            visited[i]=true
            i+=1
        return cnt
        
