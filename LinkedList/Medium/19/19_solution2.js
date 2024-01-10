 // Definition for singly-linked list.
 function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */

var removeNthFromEnd = function(head, n) {
    let prev = null; 
    let slow = head;
    let fast = head;
    for(let i = 0; i < n; i++){
        fast = fast.next;
    }
    while(fast){
        prev = slow
        slow = slow.next; 
        fast = fast.next; 
    }
    
    // the removeNode = slow;
    if(prev == null){
        head = head.next;
        return head
    }
    prev.next = slow.next; 
return head      
};