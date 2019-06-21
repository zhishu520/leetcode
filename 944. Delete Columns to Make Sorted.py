class Solution:
    def minDeletionSize(self, A):
        return sum(sorted(a) != list(a) for a in zip(*A))