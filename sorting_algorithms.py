from ds import LinkedList

def bubble_sort(theSeq):
    if isinstance(theSeq, list):
        n = len(theSeq)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if theSeq[j] > theSeq[j + 1]:
                    theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
        return theSeq

    elif isinstance(theSeq, LinkedList):
        n = len(theSeq)
        for i in range(n - 1):
            current = theSeq.head
            for _ in range(n - i - 1):
                next_node = current.next
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                current = next_node
        return theSeq

    else:
        raise TypeError(f"Unsupported type: {type(theSeq)}")
