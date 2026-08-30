class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [0] * n
        count = [0]

        def dfs(i, parent):
            if states[i] == VISITING:
                return False
            if states[i] == VISITED:
                return True
            
            states[i] = VISITING
            count[0] += 1

            for nei in adj[i]:
                if nei == parent:
                    continue
                if not dfs(nei, i):
                    return False
            return True
        
        if not dfs(0, -1):
            return False

        return count[0] == n
