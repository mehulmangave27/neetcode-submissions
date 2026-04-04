class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        res = 0

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u) 
        visit = set()

        def dfs(node):
            for j in adj[node]:
                if j not in visit:
                    visit.add(j)
                    dfs(j)

        for n in range(n):
            if n not in visit:
                dfs(n)
                res+=1
        return res    