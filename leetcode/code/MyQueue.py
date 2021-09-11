class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.output_stack:
            return self.output_stack.pop()
        else:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
            return self.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.output_stack:
            return self.output_stack[-1]
        else:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
            return self.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.output_stack and not self.input_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
