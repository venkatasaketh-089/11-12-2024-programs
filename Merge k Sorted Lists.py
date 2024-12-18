import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution(object):
    def mergeKLists(self, lists):
        min_heap = []
        
        for l in lists:
            if l:  
                heapq.heappush(min_heap, l)
        
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            smallest_node = heapq.heappop(min_heap)
            current.next = smallest_node  
            current = current.next  
            
            if smallest_node.next:
                heapq.heappush(min_heap, smallest_node.next)
        
        return dummy.next