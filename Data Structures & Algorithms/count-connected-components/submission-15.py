class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        res = [0]

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        

        for i in range(n):
            if i not in visited:
                dfs(i)
                res[0] += 1
        
        return res[0]