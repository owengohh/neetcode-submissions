class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return

        count = [0]
        for i in range(n):
            if i not in visited:
                dfs(i)
                count[0] += 1
        
        return count[0]