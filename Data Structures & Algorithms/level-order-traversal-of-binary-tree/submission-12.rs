// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//     pub val: i32,
//     pub left: Option<Rc<RefCell<TreeNode>>>,
//     pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         TreeNode {
//             val,
//             left: None,
//             right: None,
//         }
//     }
// }

use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {

        let root_node = match root {
            Some(node) => node,
            None => return vec![],
        };


        let mut res = Vec::new();
        let mut q = VecDeque::new();

        q.push_back(root_node);

        while !q.is_empty() {
            let size = q.len();
            let mut level = Vec::new();

            for _ in 0..size {
                let node = q.pop_front().unwrap();
                let node = node.borrow();

                level.push(node.val);

                if let Some(left) = node.left.clone() {
                    q.push_back(left);
                }

                if let Some(right) = node.right.clone() {
                    q.push_back(right);
                }
            }

            res.push(level)
        }

        res
    }
}
