class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.ins = []
        self.outs = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """

        self.ins.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """

        if len(self.outs) == 0:
            while len(self.ins) != 0:
                self.outs.append(self.ins.pop())

        return self.outs.pop();

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """

        if len(self.outs) == 0:
            while len(self.ins) != 0:
                self.outs.append(self.ins.pop())

        return self.outs[len(self.outs) - 1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

        return len(self.ins) == 0 and len(self.outs) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()