class Stack:
    def __init__(self) -> None:
        self.stack = list()
    
    def size(self) -> int:
        return len(self.stack)
    
    def is_empty(self) -> bool:
        return not bool(len(self.stack))
    
    def push(self, data: any) -> None:
        self.stack.append(data)

    def pop(self) -> any:
        if not self.is_empty():
            return self.stack.pop() 
    
    def peek(self) -> any:
        if not self.is_empty():
            return self.stack[-1]
    
    def __str__(self) -> str:
        return str(self.stack).replace(', ','->') \
            .replace('[','').replace(']','')

def main():
    pass
    # s = Stack()
    # s.push(1) 
    # s.push(2) 
    # s.push(3) 
    # print(s.pop()) 
    # print(s.peek()) 
    # print(s) 
    # print(s.size()) 
    # print(s.is_empty()) 

if __name__ == '__main__':
    main()

