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
        let root_node = match root {
            Some(node) => node,
            None => return None,
        };

        // swap left and right
        {
            let mut node = root_node.borrow_mut();
            let left = node.left.take();
            node.left = node.right.take();
            node.right = left;
        }

        let (left, right) = {
            let node = root_node.borrow();
            (node.left.clone(), node.right.clone())
        };
        
        // recursion
        Self::invert_tree(left);
        Self::invert_tree(right);

        Some(root_node)
    }
}
