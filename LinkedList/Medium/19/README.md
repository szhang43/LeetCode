# Remove the Nth Node from End of List
Difficulty: Medium 

## Description
Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

## Example

#### Example 1:
**Input**: head = [1,2,3,4,5], n = 2
**Output**: [1,2,3,5]

#### Example 2:
**Input** : head = [1], n = 1
**Ouput**: []

#### Example 3:
**Input**: head = [1,2], n = 1
**Output**: [1]

## Approach
The approach uses two pointers, `slow` and `fast`, to find and remove the nth node from the end of a linked list.

Initialize a `prev` pointer as null to keep track of the previous node.  Then creating a `slow`, and `fast` pointer, both pointing to the head of the linked list.
Moving the `fast` pointer n steps ahead, it creates a gap of n nodes between `slow` and `fast`.

Iterate with both pointers until `fast` reaches the end of the list. This allows the `slow` pointer to be positioned at the nth node from the end.

Then we can remove the nth node by updating the `prev.next` pointer.

#### Edge Cases
If `prev` is still null after the loop, it means the head itself needs to be removed. In this case, update the head to point to the next node.

## Time Complexity
The time complexity of this approach is O(n), where n is the number of nodes in the linked list. The algorithm iterates through the list twice: once to move the `fast` pointer n steps ahead and once to find and remove the nth node. Since the number of operations scales linearly with the number of nodes, the time complexity is O(n).