class Node:
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

        def insert(self,newNode):
            if(self.head == None):
                self.head = newNode
            else:
                self.head.next = newNode
                lastNode = self.head
                while True:
                    if lastNode.next is None:
                        break
                    lastNode = lastNode.next
                lastNode.next = newNode

        def printList(self):
            currentNode = self.head
            while True:
                if currentNode is None:
                    break;
                print(currentNode.data)
                currentNode = currentNode.next