// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
//
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {

        let mut head_node = match head {
            Some(node) => node,
            None => return None,
        };

        let mut curr = Some(&head_node);
        let mut count = 0;

        while let Some(node) = curr {
            curr = node.next.as_ref();
            count += 1;
        }

        if count == n {
            return head_node.next
        }

        let idx_remove = count - n - 1;
        let mut curr = &mut head_node;

        for i in 0..idx_remove {
            curr = curr.next.as_mut().unwrap();
        }
        
        if let Some(mut removed_node) = curr.next.take() {
            curr.next = removed_node.next.take()
        }

        Some(head_node)
    }
}
