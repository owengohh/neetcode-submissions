class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count