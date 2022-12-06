class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self) -> str:
        return str(self.data)

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def size(self) -> int:
        size = 0
        run = self.head
        while run:
            size += 1
            run = run.next
        return size
    
    def is_empty(self) -> bool:
        return not bool(self.head)
    
    def append(self, data: any) -> None:
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    
    def add_head(self, data: any) -> None:
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def insert(self, index: int, data: any) -> None:
        node = Node(data)
        size = self.size()
        if (self.is_empty() and index == 0) or index == size:
            self.append(data)
        elif index == 0:
            node.next = self.head.next
            self.head.next.prev = node
            self.head = node
        elif index == size - 1:
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail = node
        elif index > 0 and index < size-1:
            run = self.head
            for _ in range(index-1):
                run = run.next
            node.next = run.next
            node.prev = run
            run.next.prev = node
            run.next = node
    
    def remove_index(self, index: int) -> None:
        size = self.size()
        if self.is_empty():
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        if index == size - 1: 
            self.tail = self.tail.prev
            self.tail.next = None
        elif index > 0 and index < size - 1:
            run = self.head
            for _ in range(index-1):
                run = run.next
            temp = run.next.next
            run.next = run.next.next
            temp.prev = run
    
    def remove_data(self, data: any) -> None:
        run = self.head
        if self.is_empty():
            return
        if run.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        while run:
            if run.data == data:
                break
            prev = run
            run = run.next
        if not run:
            return
        prev.next = run.next
        if self.tail.data != data:
            run.next.prev = prev
        else:
            self.tail = prev
    
    def str_rev(self) -> str:
        if self.is_empty():
            return "List is Empty"
        else:
            ret = str(self.tail.data)
            run = self.tail.prev
            while run:
                ret += f"<-{run.data}"
                run = run.prev
            return ret
    
    def __str__(self) -> str:
        if self.is_empty():
            return "List is Empty"
        else:
            ret = str(self.head.data)
            run = self.head.next
            while run:
                ret += f"->{run.data}"
                run = run.next
            return ret

def main():
    pass
    # dll = DoublyLinkedList()
    # dll.append(0)
    # dll.append(1)
    # dll.append(2)
    # dll.add_head(3)
    # dll.insert(1,5)
    # dll.remove_index(0)
    # dll.remove_data(5)
    # print(dll)
    # print(dll.str_rev())
    # print(dll.size())
    # print(dll.is_empty())

if __name__ == '__main__':
    main()



