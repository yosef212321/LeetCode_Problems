class MyQueue:

    def __init__(self):
        self.queue = []
        self.reverse = []
    def push(self, x: int) -> None:
        self.queue.append(x)
    def pop(self) -> int:
        while self.queue:
            self.reverse.append(self.queue.pop())
        temp = self.reverse[-1]
        self.reverse.remove(temp)
        while self.reverse:
            self.queue.append(self.reverse.pop())
        return temp
    def peek(self) -> int:
        return self.queue[0]
    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
