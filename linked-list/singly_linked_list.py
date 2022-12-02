class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def size(self) -> int:
        if not self.head:  
            return 0
        size = 0
        run = self.head
        while run:
            size += 1
            run = run.next
        return size

    def is_empty(self) -> bool:
        return False if self.head else True

    def append(self, data: any) -> None:
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
    
    def add_head(self, data: any) -> None:
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
    
    def insert(self, index: int, data: any) -> None:
        node = Node(data)
        size = self.size()
        if (size == 0 and index == 0) or index == size:
            self.append(data)
        elif index == 0:
            node.next = self.head.next
            self.head = node
        elif index > 0 and index < size:
            run = self.head
            for _ in range(index-1):
                run = run.next
            node.next = run.next.next
            run.next = node
    
    def remove_index(self, index: int) -> None:
        size = self.size()
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
        elif index > 0 and index < size:
            run = self.head
            for _ in range(index-1):
                run = run.next
            run.next = run.next.next
            if index == size-1:
                self.tail = run
    
    def remove_data(self, data: any) -> None:
        run = self.head
        if self.is_empty():
            return
        if run.data == data:
            self.head = self.head.next
            return
        while run:
            if run.data == data:
                break
            prev = run
            run = run.next
        if not run:
            return
        prev.next = run.next
        if self.tail.data == run.data:
            self.tail = prev

    def __str__(self) -> str:
        if self.head:
            ret = str(self.head.data)
            run = self.head.next 
            while run:
                ret += f"->{run.data}"
                run = run.next
            return ret
        else:
            return "List is Empty"

def main():
    pass
    # sll = SinglyLinkedList()
    # sll.append(0)
    # sll.append(1)
    # sll.append(2)
    # sll.add_head(3) 
    # sll.insert(1,5)
    # sll.remove_index(0)
    # sll.remove_data(5)
    # print(ll)
    # print(ll.size())
    # print(ll.is_empty())

if __name__ == '__main__':
    main()

