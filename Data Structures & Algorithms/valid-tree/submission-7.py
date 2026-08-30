class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for e in edges:
            n1, n2 = e
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        UV = 0
        VISITING = 1
        VISITED = 2

        states = [UV] * n
        visited_count = [0]

        def dfs(node, parent):
            if states[node] == VISITING: return False
            if states[node] == VISITED: return True

            states[node] = VISITING
            visited_count[0] += 1

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            states[node] = VISITED

            return True
        
        if not dfs(0, -1):
            return False
        return visited_count[0] == n 