
class RecentCounter(object):

    def __init__(self):
        self.li = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        while len(self.li) > 0 and t - 3000 > self.li[0]:
            self.li.pop(0)

        self.li.append(t)
        return len(self.li)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)