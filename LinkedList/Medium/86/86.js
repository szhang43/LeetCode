
// Definition for singly-linked list.
function ListNode(val, next) {
     this.val = (val===undefined ? 0 : val)
     this.next = (next===undefined ? null : next)
 }

/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    let less = null; 
    let greater = null; 
    let curr = head; 
    let compare = head; 
    while(compare.val != x){
        compare = compare.next;
    }
    while(curr){
        if(curr.val < compare.val){
            console.log("Less")
            console.log("Current:", curr.val, "Compare:", compare.val)
            if(!less){
                less = curr
            } else {
                less.next = curr
            }
        } else {
            console.log("Greater")
            console.log("Current:", curr.val, "Compare:", compare.val)
            if(!greater){
                greater = curr
            } else{
            greater.next = curr
            }
        }
        curr = curr.next; 
    }
    console.log("Less:", less, "Greater:", greater)
    
};

partition([1, 4, 3, 2, 5, 2], x = 3);