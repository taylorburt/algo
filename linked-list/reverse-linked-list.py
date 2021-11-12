# a -> b -> c -> d -> None
# d -> c -> b -> a -> None

def reverseLinkedList(head):
    lookBack = None
    current = head
    lookNext = None
    # currentObject = None
    while True:
        print(current.getValue())
        lookNext = current.getNext()
        if current.getValue() == head.getValue():
            head.setNext(None)
        elif current.getNext() == None:
            current.setNext(lookBack)
            break
        else:
            current.setNext(lookBack)

        lookBack = current
        current = lookNext

    return current


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


current = reverseLinkedList(linkedListA)

print("\nSolution\n")


while True:
    print(current.getValue())
    if current.getNext() == None:
        break
    else:
        current = current.getNext()