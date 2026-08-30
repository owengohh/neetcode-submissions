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
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let root_node = root?;

        let (left, right) = {
            let mut node = root_node.borrow_mut();
            (node.left.take(), node.right.take())
        };

        {
            let mut node = root_node.borrow_mut();
            node.left = Self::invert_tree(right);
            node.right = Self::invert_tree(left);
        }

        Some(root_node)
    }
}
