class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(pos,visited):
            if pos>n:
                return 1
            count=0
            for i in range(1,n+1):
                if not visited[i-1] and (i%pos==0 or pos%i==0):
                    visited[i-1]=True
                    count+=backtrack(pos+1,visited)
                    visited[i-1]=False
            return count

        visited=[False]*n
        return backtrack(1,visited)


