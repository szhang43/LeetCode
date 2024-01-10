
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

var get = function(head, n){
    let temp = head; 
    if(n < 0){
        return false
    }
    for(let i = 0; i< n; i++){
        temp = temp.next;
    }
    return temp;
}

var removeNthFromEnd = function(head, n) {
    let count = 0; 
    let temp = head;
    while(temp){
        temp = temp.next;
        count++;
    }
    if(count === 1) return null;
    let prev = get(head, count - n - 1) 
    let removeNode = get(head, count - n); 

    if(!prev){
        head = head.next; 
        return head;
    }
    prev.next = removeNode.next; 
    return head;

};

