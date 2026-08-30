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

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let root_node = match root {
            Some(node) => node,
            None => return 0,
        };

        let (left, right) = {
            let node = root_node.borrow();
            (node.left.clone(), node.right.clone())
        };

        let left_depth = Self::max_depth(left);
        let right_depth = Self::max_depth(right);

        1 + left_depth.max(right_depth)
    }
}
