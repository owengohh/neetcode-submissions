class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        count = [0]

        states = [0] * n

        def dfs(n):
            if states[n] == 1:
                return
            states[n] = 1
            for nei in adj[n]:
                dfs(nei)
            return
        
        for i in range(n):
            if states[i] == 0:
                dfs(i)
                count[0] += 1
        
        return count[0]
                