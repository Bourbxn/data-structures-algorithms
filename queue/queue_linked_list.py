class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data) 

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
    
    def __len__(self) -> int:
        size = 0
        run = self.front
        while run:
            size += 1
            run = run.next
        return size 

    def __iter__(self) -> None:
        run = self.front
        while run:
            yield run
            run = run.next
    
    def __str__(self) -> str:
        if self.is_empty():
            return "Queue is Empty"
        else:
            return '->'.join([str(node) for node in self])
    
    def is_empty(self) -> bool:
        return not bool(self.front)
    
    def enqueue(self, data: any) -> None:
        node = Node(data)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self) -> any:
        if not self.is_empty():
            ret = self.front
            self.front = ret.next
            return ret.data
    
    def get_front(self) -> any:
        if not self.is_empty():
            return self.front.data
    
    def get_rear(self) -> any:
        if not self.is_empty():
            return self.rear.data
            
def main():
    pass
    # q = Queue()
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)
    # print(q.dequeue())
    # print(q)
    # print(q.get_front())
    # print(q.get_rear())
    # print(len(q))
    # print(q.is_empty())

if __name__ == '__main__':
    main()
    

