class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """


        cnt =  len(s) / k

        r = ""
        for i in range(cnt):
            if cnt % 2 == 1:
                r += s[k*i:k*(i+1)]
                print 1, r
            else:
                r += s[k*i:k*(i+1)][::-1]
                print 0, r

        return r
