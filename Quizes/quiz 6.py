# Written by Subham Anand

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        node = self.head
        myHead = self.head
        #print(node.value)
        while node:
            lastNode = node
            node = node.next_node
        newLast = lastNode
        #print(newLast.value)
        while myHead.value % 2 == 0 and myHead != lastNode :
            newLast.next_node = myHead
            myHead = myHead.next_node
            newLast.next_node.next_node = None
            newLast = newLast.next_node
        #print(newLast.value)
        if myHead.value % 2 != 0:
            self.head = myHead
            while myHead != lastNode:
                if myHead.value % 2 != 0:
                    prev = myHead
                    myHead = myHead.next_node
                    #print(prev.value)
                else:
                    prev.next_node = myHead.next_node
                    myHead.next_node = None
                    newLast.next_node = myHead
                    newLast = myHead
                    myHead = prev.next_node
                    #print(myHead.value)
            #print(myHead.value)
        else:
            prev = myHead
        if newLast != lastNode and lastNode.value % 2 == 0:
            prev.next_node = lastNode.next_node
            lastNode.next_node = None
            newLast.next_node = lastNode
        #print(LL.print())
        #print(myHead.value)
        # Replace pass above with your code
    
    
    
