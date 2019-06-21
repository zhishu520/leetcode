class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        cnts = [0] * 26

        for i in chars:
            cnts[ord(i) - ord('a')] += 1

        ret = 0
        tcnt = 0

        for i in range(len(cnts)):
            if cnts[i] == 0:
                pass
            elif cnts[i] == 1:
                ret += 1
                chars[tcnt] = chr(ord('a') + i)
                tcnt += 1
            else:

                chars[tcnt] = chr(ord('a') + i)

                while cnts[i] > 0:
                    cnts[i] /= 10
                    ret += 1

        return ret











