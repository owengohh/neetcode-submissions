impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let n = num_courses as usize;
        let mut graph = vec![Vec::new(); n];
        let mut indegree =  vec![0; n];

        for prerequisite in prerequisites {
            let course = prerequisite[0] as usize;
            let required = prerequisite[1] as usize;

            graph[required].push(course);
            indegree[course] += 1;
        }

        let mut q = VecDeque::new();

        for course in 0..n {
            if indegree[course] == 0 {
                q.push_back(course);
            }
        }

        let mut completed = 0;
        while let Some(course) = q.pop_front() {
            completed += 1;

            for &next_course in &graph[course] {
                indegree[next_course] -= 1;

                if indegree[next_course] == 0 {
                    q.push_back(next_course);
                }
            }
        }

        completed ==n
    }
}
