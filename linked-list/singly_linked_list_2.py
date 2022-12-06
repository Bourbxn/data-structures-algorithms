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
    
    def __len__(self) -> int:
        size = 0
        run = self.head
        while run:
            size += 1
            run = run.next
        return size
    
    def __iter__(self) -> None:
        run = self.head
        while run:
            yield run
            run = run.next
    
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
            self.tail.next = node
            self.tail = node
    
    def add_head(self, data: any) -> None:
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
    
    def insert(self, index: int, data: any) -> None:
        node = Node(data)
        size = len(self)
        if (size == 0 and index == 0) or index == size:
            self.append(data)
        elif index == 0:
            node.next = self.head
            self.head = node
        elif index > 0 and index < size:
            temp = self.node(index-1)
            node.next = temp.next
            temp.next = node
    
    def remove_index(self, index: int) -> None:
        size = len(self)
        if self.is_empty():
            return
        if index == 0:
            self.head = self.head.next
        elif index > 0 and index < size:
            temp = self.node(index-1)
            temp.next = temp.next.next
            if index == size-1:
                self.tail = temp
    
    def remove_data(self, data: any) -> None:
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        for node in self:
            if node.next and node.next.data == data:
                temp = node.next
                node.next = node.next.next
                if self.tail.data == temp.data:
                    self.tail = node
                break

def main():
    pass
    # sll = SinglyLinkedList()
    # sll.append(0)
    # sll.append(1)
    # sll.append(2)
    # sll.add_head(3) 
    # sll.insert(1,5)
    # sll.remove_index(2)
    # sll.remove_data(2)
    # print(sll)
    # print(sll.node(1))
    # print(len(sll))
    # print(sll.is_empty())

if __name__ == '__main__':
    main()

