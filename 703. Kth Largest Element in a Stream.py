class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        nums.sort(reverse=True)
        self.list = nums[0:k]
        self.max = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        l = len(self.list)

        if l == self.max and val <= self.list[l - 1]:
            return self.list[l - 1]

        binsert = False
        for i in range(l):
            if val > self.list[i]:
                self.list.insert(i, val)
                binsert = True
                l += 1
                break

        if not binsert and l < self.max:
            self.list.append(val)
            l += 1

        if l > self.max:
            self.list.pop()
            l -= 1
        return self.list[l - 1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)