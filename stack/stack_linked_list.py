class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)

class Stack:
    def __init__(self) -> None:
        self.top = None
    
    def __len__(self) -> None:
        size = 0
        run = self.top
        while run:
            size += 1
            run = run.next
        return size 
    
    def __iter__(self) -> None:
        run = self.top
        while run:
            yield run
            run = run.next
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Stack is Empty"
        else:
            return '->'.join([str(node) for node in self])
    
    def is_empty(self) -> bool:
        return not bool(self.top)
    
    def push(self, data: any) -> None:
        node = Node(data)
        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def pop(self) -> any:
        if not self.is_empty():
            ret = self.top
            self.top = ret.next
            return ret.data
    
    def peek(self) -> any:
        if not self.is_empty():
            return self.top.data

def main():
    pass
    # s = Stack()
    # s.push(1) 
    # s.push(2) 
    # s.push(3) 
    # print(s.pop())
    # print(s)
    # print(s.peek())
    # print(len(s))
    # print(s.is_empty())

if __name__ == '__main__':
    main()