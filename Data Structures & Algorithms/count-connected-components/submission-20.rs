impl Solution {
    pub fn count_components(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        fn dfs(
            n: usize,
            graph: &[Vec<usize>],
            visited: &mut HashSet<usize>
        ) -> bool {
            if visited.contains(&n) {
                return false;
            }

            visited.insert(n);
            for &nei in &graph[n] {
                dfs(nei, graph, visited);
            }

            true
        }

        let num = n as usize;
        let mut graph = vec![Vec::new(); num];
        
        for edge in edges {
            let node1 = edge[0] as usize;
            let node2 = edge[1] as usize;

            graph[node1].push(node2);
            graph[node2].push(node1);
        }

        let mut count = 0;
        let mut visited: HashSet<usize> = HashSet::new();

        for i in 0..num {
            if dfs(i, &graph, &mut visited) {
                count += 1;
            }
        }

        count

    }
}
