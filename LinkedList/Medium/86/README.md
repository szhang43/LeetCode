# 86. Partition List
Difficulty: Medium 

## Description
Given the `head` of a linked list and a value `x`, partition it such that all nodes less than x come before nodes greater than or equal to `x`.

You should preserve the original relative order of the nodes in each of the two partitions.

## Example

#### Example 1:
**Input**: head = [1,4,3,2,5,2], x = 3
**Output**: [1,2,2,4,3,5]

#### Example 2:
**Input** : head = [2,1], x = 2
**Ouput**: [1, 2]

## Approach
The `partition` function begins by initializing two dummy nodes, `dummy1` and `dummy2`, representing the heads of two linked lists. Additionally, it sets up pointers `less` and `greater` to keep track of the current positions in these linked lists. The `curr` pointer starts at the head of the original linked list.

As it traverses the original list, each node is compared. If the node's value is less than `x`, it is appended to the "less" linked list. If the value is greater than or equal to `x`, the node is appended to the "greater" linked list.

After traversing, the "greater" list's next pointers are set to null. Then, the "less" list is connected to the head of the "greater" list, merging the two partitions.

The resulting linked list, starting from the next node of the dummy node in the "less" linked list, represents the partitioned list with nodes rearranged based on their values in relation to `x`.

## Time Complexity

The time complexity of the `partition` function is O(N), where N is the number of nodes in the linked list. It iterates through each node once, performing constant-time operations for each node.