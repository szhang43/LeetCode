/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    let dummy = new ListNode(); 
    dummy.next = head; 
    let prev = dummy; 
    let curr = dummy.next; 
    let next = curr.next;
    
    for(let i = 0; i < left - 1; i++){
        prev = prev.next; 
        curr = curr.next;
        next = next.next
    }

    for(let i = 0; i < right - left; i++){
        next = curr.next; 
        curr.next = next.next; 
        next.next = prev.next; 
        prev.next = next
    }
    return dummy.next;
};