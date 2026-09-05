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
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::validate(root, None, None)
    }

    fn validate(
        root: Option<Rc<RefCell<TreeNode>>>,
        min: Option<i32>,
        max: Option<i32>,
    ) -> bool {
        let root_node = match root {
            Some(node) => node,
            None => return true,
        };

        let (val, left, right) = {
            let node = root_node.borrow();
            (node.val, node.left.clone(), node.right.clone())
        };

        if let Some(min_value) = min {
            if val <= min_value {
                return false;
            }
        }

        if let Some(max_value) = max {
            if val >= max_value {
                return false;
            }
        }

        Self::validate(left, min, Some(val)) && Self::validate(right, Some(val), max)

    }
}
