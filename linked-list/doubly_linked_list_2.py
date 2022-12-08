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
    
    def __iter__(self) -> None:
        run = self.head
        while run:
            yield run
            run = run.next
    
    def __reversed__(self) -> None:
        run = self.tail
        while run:
            yield run
            run = run.prev
    
    def __len__(self) -> int:
        size = 0
        for _ in self:
            size += 1
        return size

    def __str__(self) -> str:
        if self.is_empty():
            return "List is Empty"
        else:
            return '->'.join([str(node) for node in self])
    
    def node(self, index: int) -> Node:
        for i, node in enumerate(self):
            if i == index:
                return node
    
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
        size = len(self)
        if (self.is_empty() and index == 0) or index == size:
            self.append(data)
        elif index == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif index == size - 1:
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
        elif index > 0 and index <= size-1:
            temp = self.node(index-1)
            node.next = temp.next
            node.prev = temp
            temp.next.prev = node
            temp.next = node
    
    def remove_index(self, index: int) -> None:
        size = len(self)
        if self.is_empty():
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        if index == size - 1: 
            self.tail = self.tail.prev
            self.tail.next = None
        elif index > 0 and index < size - 1:
            prev = self.node(index-1)
            temp = prev.next.next
            prev.next = prev.next.next
            temp.prev = prev
    
    def remove_data(self, data: any) -> None:
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        if self.tail.data == data:
            temp = self.tail.prev
            self.tail.prev = None
            temp.next = None
            self.tail = temp
        for node in self:
            if node.next and node.next.data == data:
                temp = node.next.next
                node.next = temp
                temp.prev = node
                break
    
    def str_rev(self) -> str:
        if self.is_empty():
            return "List is Empty"
        else:
            return '<-'.join([str(node) for node in reversed(self)])

def main():
    pass
    # dll = DoublyLinkedList()
    # dll.append(0)
    # dll.append(1)
    # dll.append(2)
    # dll.add_head(3)
    # dll.insert(2,5)
    # dll.remove_index(4)
    # dll.remove_data(1)
    # print(dll)
    # print(dll.str_rev())
    # print(len(dll))
    # print(dll.is_empty())

if __name__ == '__main__':
    main()



