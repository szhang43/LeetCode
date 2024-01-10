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
var middleNode = function(head) {
    let count = 0;
    let tmp = head;
    while(tmp){
        count++;
        tmp = tmp.next;
    }
    tmp = head;
    for(let i = 0; i < (Math.floor(count/2)); i++){
        tmp = tmp.next;
    }
    return tmp
};