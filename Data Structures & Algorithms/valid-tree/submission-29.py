class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        states = [0] * n
        count = [0]

        def dfs(node, parent):
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True
            states[node] = 1
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            states[node] = 2
            count[0] += 1
            return True
        
        if not dfs(0, -1):
            return False
        return count[0] == n