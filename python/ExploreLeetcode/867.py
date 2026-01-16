# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arrayList = []
        count = 0
        while head != None:
            count += 1
            arrayList.append(head)
            head = head.next
        
        return arrayList[count/2]
            
# TC: O(n)
# SC: O(n)





# Using two pointer to jump and get the middle node. 
# Advice: starting from the easiest case of 1 node 
# and go up to see the patterns
# We move up middle node after two jump of current node
    def middleNodeV2(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        middleNode = head
        endNode = head
        while (endNode != None and endNode.next != None):
            middleNode = middleNode.next
            endNode = endNode.next.next
            
        return middleNode
          
# TC: O(n)
# SC: O(1)
      
      
      
           

if __name__ == "__main__":
    s = Solution()
    s.middleNode()
    
    
