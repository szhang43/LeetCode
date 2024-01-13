# 92. Merge Two Sorted Lists
Difficulty: Easy

## Description
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


## Example

#### Example 1:
**Input**: list1 = [1,2,4], list2 = [1,3,4]
**Output**: [1,1,2,3,4,4]

#### Example 2:
**Input** : list1 = [], list2 = [0]
**Ouput**: [0]

## Approach
Create a dummy node using the ListNode funtion to create another instance of the list. This will allow us to keep track of the original list. 

Then we will traverse through both lists at the same time using a while loop with the condition `while(list1 && list2)`. Then we will compare the values from `list1` and `list2`. Depending on which value is larger, it will be spliced into the original linked list. 

After this while loop is finished running, we would have to check if there are remaining values in either of the lists. If there is, it would be added on at the end. 

Finally, we return `dummy.next`

## Time Complexity
The time complexity of the provided code is `O(m + n)`, where m and n are the lengths of the input linked lists list1 and list2. The code iterates through both lists once, comparing and merging nodes in sorted order.