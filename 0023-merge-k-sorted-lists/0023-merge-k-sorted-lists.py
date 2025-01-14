# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        currentNode = head
        lists2 = []
        for lst in lists:
            if lst is not None: lists2.append(lst)
        while len(lists2) > 0:
            minVal = lists2[0].val
            minI = 0
            for i in range(len(lists2)):
                if lists2[i].val < minVal:
                    minVal = lists2[i].val
                    minI = i
            currentNode.next = ListNode()
            currentNode = currentNode.next
            currentNode.val = minVal
            if lists2[minI].next is None:
                lists2.pop(minI)
            else:
                lists2[minI] = lists2[minI].next
        return head.next
        