#[derive(Clone, Copy, PartialEq)]
enum State {
    Unvisited,
    Visiting,
    Completed,
}

impl Solution {
    pub fn valid_tree(n: i32, edges: Vec<Vec<i32>>) -> bool {

        fn dfs(
            n: usize,
            parent: Option<usize>,
            graph: &[Vec<usize>],
            states: &mut [State],
            count: &mut usize
        ) -> bool {
            match states[n] {
                State::Visiting => return false,
                State::Completed => return true,
                State::Unvisited => {}
            }

            states[n] = State::Visiting;

            for &nei in &graph[n] {
                if Some(nei) == parent {
                    continue;
                }

                if !dfs(nei, Some(n), graph, states, count) {
                    return false;
                } 
            }

            states[n] = State::Completed;
            *count += 1;
            true
        }

        let num = n as usize;
        let mut graph = vec![Vec::new(); num];
        for edge in edges {
            let n1 = edge[0] as usize;
            let n2 = edge[1] as usize;
            graph[n1].push(n2);
            graph[n2].push(n1);
        }

        let mut states = vec![State::Unvisited; num];
        let mut count = 0;

        if !dfs(0, None, &graph, &mut states, &mut count) {
            return false;
        }

        count == num
    
    }
}
