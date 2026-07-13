class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        
        return -1
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.head is self.tail:
            self.tail = new_node
    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next
    def remove(self, index: int) -> bool:
        if index < 0:
            return False
        
        curr = self.head
        i = 0
        while i < index and curr.next:
            curr = curr.next
            i += 1
        
        if curr.next is None:
            return False
        
        if curr.next is self.tail:
            self.tail = curr
        
        curr.next = curr.next.next
        return True
    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
