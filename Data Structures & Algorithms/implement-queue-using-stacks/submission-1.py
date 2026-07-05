class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []
        self.peekE1 = -1

    def push(self, x: int) -> None:
        if not self.input:
            self.peekE1 = x
        return self.input.append(x)

    def pop(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            return self.peekE1
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()