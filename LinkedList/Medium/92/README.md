## 92. Reverse Linked List II
Difficulty: Medium 

### Description
Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.


### Example: 

**Input**: head = [1,2,3,4,5], left = 2, right = 4
**Output**: [1,4,3,2,5]

<br>

**Input** : head = [5], left = 1, right = 1
**Ouput**: [5]


### Approach

Create a dummy node using the provided ListNode function. The idea is to keep track of the previous pointer `prev`, current pointer `curr`, and the next pointer `next`. The curr pointer should be positioned at the node before the section to be reversed.

Then, using another loop, reverse the nodes from the left to the right. Keep track of the previous and next nodes during this process. 

Finally, connect the reversed part back to the original list, and return the dummy.next.