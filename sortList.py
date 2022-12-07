# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        temp =[];
        current = head
        if head is not None:
            while current:
                temp.append(current.val)
                current = current.next;  
        
            temp.sort();
            i=0;
            head= ListNode(temp[0]);
            current = head;
            for i in range(1,len(temp), +1):
                current.next = ListNode(temp[i]);
                current = current.next;
                i+=1;
            return head; 


                    

            
            
                