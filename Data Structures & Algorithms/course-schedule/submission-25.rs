#[derive(Clone, Copy, PartialEq)]
enum State {
    Unvisited,
    Visiting,
    Completed,
}


impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {

        fn has_cycle(
            course: usize,
            graph: &[Vec<usize>],
            states: &mut [State],
        ) -> bool {
            match states[course] {
                State::Visiting => return true,
                State::Completed => return false,
                State::Unvisited => {}
            }

            states[course] = State::Visiting;

            for &prequisite in &graph[course] {
                if has_cycle(prequisite, graph, states) {
                    return true;
                }
            }

            states[course] = State::Completed;
            false
        }

        let course_count = num_courses as usize;

        let mut graph = vec![Vec::new(); course_count];

        for edge in prerequisites {
            let course = edge[0] as usize;
            let prereq = edge[1] as usize;
            graph[course].push(prereq);
        }

        let mut states = vec![State::Unvisited; course_count];

        (0..course_count).all(|course| !has_cycle(course, &graph, &mut states))
    }
}
