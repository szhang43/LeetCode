/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    let dummy1 = new ListNode();
    let dummy2 = new ListNode(); 
    let less = dummy1; 
    let greater = dummy2;
    let curr = head; 

    while(curr !== null){
        if(curr.val < x){
            less.next = curr;
            less = less.next;
        } else {
            greater.next = curr;
            greater = greater.next;
        }
        curr = curr.next; 
    }
    
    greater.next = null; 
    less.next = dummy2.next;

    return dummy1.next
};
