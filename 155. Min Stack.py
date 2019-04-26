class MinStack(object):

    def __init__(self):
        self.a = []
        self.m = []

    def push(self, x):
        l = len(self.a)
        self.a.append(x)
        self.m.append(x if l == 0 or x < self.m[l - 1] else self.m[l - 1])

    def pop(self):
        self.a.pop()
        self.m.pop()

    def top(self):
        l = len(self.a)
        return self.a[l - 1]

    def getMin(self):
        l = len(self.a)
        return self.m[l - 1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()