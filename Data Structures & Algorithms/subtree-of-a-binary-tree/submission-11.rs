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
    pub fn is_subtree(root: Option<Rc<RefCell<TreeNode>>>, sub_root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if sub_root.is_none() {
            return true;
        }

        let root_node = match root {
            Some(node) => node,
            None => return false,
        };

        if Self::is_same_tree(Some(root_node.clone()), sub_root.clone()) {
            return true;
        }

        let(left, right) = {
            let node = root_node.borrow();
            (node.left.clone(), node.right.clone())
        };

        Self::is_subtree(left, sub_root.clone()) || Self::is_subtree(right, sub_root.clone())

    }
    
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match (p, q) {
            (None, None) => true,
            (Some(p), Some(q)) => {
                let(p_val, p_left, p_right) = {
                    let node = p.borrow();
                    (node.val, node.left.clone(), node.right.clone())
                };

                let (q_val, q_left, q_right) = {
                    let node = q.borrow();
                    (node.val, node.left.clone(), node.right.clone())
                };

                p_val == q_val && Self::is_same_tree(p_left, q_left) && Self::is_same_tree(p_right, q_right)
            }
            _ => false,
        }
    }
}
