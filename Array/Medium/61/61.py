# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
class Solution:
  def count_length(self, head): 
    curr = head
    count = 0
    while curr: 
        count += 1
        curr = curr.next
    return count
  
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      count = self.count_length(head)
      if not head or not head.next: 
          return head
      tempHead = head 
      curr = head 
      prev = ListNode()
      for i in range(k % count):
          while curr.next: 
              prev = curr
              curr = curr.next
          prev.next = None
          curr.next = tempHead
          tempHead = curr
      return curr
      
        
          
              


    
    
linkList1 = Solution().list_to_linked_list([1,2,3,4,5])
set1 = Solution().rotateRight(linkList1, 2)
print(set1)

