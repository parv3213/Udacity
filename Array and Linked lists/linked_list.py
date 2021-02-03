#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

#Main
lList = LinkedList()
lList.head = Node(1)
second = Node(2)
third = Node(3)

lList.head.next = second
second.next = third

lList.printList()

print ("Complete")