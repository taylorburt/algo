# a -> b -> c -> d -> None
# d -> c -> b -> a -> None

def removeLinkedList(head, removable):
    first = LinkedList(None)
    first.setNext(head)
    prev = first
    curr = head
    while curr:
        nxt = curr.getNext()
        if curr.getValue() == removable:
            prev.setNext(nxt)
        else:
            prev = curr
        curr = nxt
    return first.getNext()


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, value):
        self.next = value

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

linkedListA = LinkedList("A")
linkedListB = LinkedList("B")
linkedListC = LinkedList("C")
linkedListD = LinkedList("D")

linkedListA.setNext(linkedListB)
linkedListB.setNext(linkedListC)
linkedListC.setNext(linkedListD)


current = removeLinkedList(linkedListA, "B")

print("\nSolution\n")


while True:
    print(current.getValue())
    if current.getNext() == None:
        break
    else:
        current = current.getNext()