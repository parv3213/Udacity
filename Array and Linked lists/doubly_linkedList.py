class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def printElements(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
    def printReverse(self):
        temp = self.tail
        while (temp):
            print (temp.data)
            temp = temp.previous
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.previous = new_node
            if self.head.next is None:
                self.tail = self.head
        self.head = new_node

    def insertAfter(self, prev_node, data):
        if prev_node is None:
            print ("Node does not exits")
        temp = prev_node.next
        new_node = Node(data)
        prev_node.next = new_node
        new_node.previous = prev_node
        new_node.next = temp
        if new_node.next != None:
            temp.previous = new_node

#Main
dLinkedList = DoubleLinkedList()
dLinkedList.push(1)
dLinkedList.push(2)
dLinkedList.push(4)
dLinkedList.insertAfter(dLinkedList.head, 3)

dLinkedList.printElements()
print("\n")
dLinkedList.printReverse()