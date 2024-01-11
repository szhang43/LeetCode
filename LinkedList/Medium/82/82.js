/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    let dummy = new ListNode()
    dummy.next = head
    let prev = dummy; 
    let curr = prev.next;
    let next;
    if(!curr.next){
        return head;
    }
    next = curr.next

    while(curr && next){
        if(curr.val == next.val){
            let tempVal = curr.val
            while(next && curr.val == tempVal){
                curr = next
                next = next.next
                prev.next = curr
            }
        }else{
            prev = prev.next
            curr = curr.next
            next = next.next
        }
    }
    return dummy.next
};