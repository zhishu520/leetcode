class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """


        bits.pop()
        l = len(bits)


        while len(bits) > 0:
            t = bits.pop(0)
            if t == 1:
                if len(bits) == 0:
                    return False
                else:
                    bits.pop(0)

        return True

if __name__ == '__main__':
    print Solution().isOneBitCharacter([1,0,0])


