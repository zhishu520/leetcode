class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        l = len(S)
        R = []
        for i in range(l+1):
            R.append(i)

        r = []

        t = S.count('D')

        for i in S:
            r.append(R[t])
            R.pop(t)

            if i == 'D':
                t -= 1

        r.append(R[0])
        return r




if __name__ == '__main__':
    s = Solution()
    r = s.diStringMatch("IIDIIDDDIDIDIDIDIDDIDDDDDIIIDIIDIIIIDIIDDIIIDIIIDDDIIIDIIDDIIDDIDDIDIDIIDIDIIIDIIIDIDDDDIIDDDIIDDDDDIIDDIDIIDIIIDDDIDIIIDIIIDIDIDDIDDIIDDDDDDDIIIDIDIIIDIDDDIDDIIIDIDDIDDIIDDDDIDIDIDIDIDIDDDDIDDDDIIDIIIDDDIDDDDDDDIDIDDDIDIDIDDDDIDIDDDDIDDIIDDIIIIDIDIIIDDDIDIIIIDDIIDIDDDIDIIDDIDDDIIIDIIDIIDIIDDIIIIIDIIDIDIDIIIDIIIDIDIIIDDDIDIIIDIDIDIIDDIIDDIIDDDDDDDIDDIIIDDDDIDDDDIDDIDDDIIIDIDIIIDDDDDDDDDDDIIDIIDDIIIIIDIIDDDDIDDIDIDIIIIDIDIIIDIIDIIIIIDIDDIDDIDDDDIDIIDIIIIDDDDIDDDIIDDDIIDDIIDIIIIIIDDIIDDIIIIIDDDDIIDDDDDIDIIDDIDIDIIDDDIDDIIIDIDDDIIDIDIIIDDIIDIDIIIIDIDDIIDIIIIIDIIIDIIDDIIIDDDDIIIIDDDIDDIDDDIDDDIDDDDDDIIIIDIIIIIDDDIDIIDDIIIDIDIIDIDIIIIDIDDDIIIIDDIDDIDDDDIDIDIIDDIDDIIIIIDIIDIIDDDDDDIIIIIDDDDIDDDDIIIDIIIDIIIDIDIDDIIIIDDDDDIDDIDDIIIIIDIDIDDIDIIIDDDDIDDDDDDDDIIDDDDIIDDDDDIDIDDIDDDDIIIDIDIDDDDIDIDIIDDIDIIIDDDDDDDDDDDDDDIDDDIIIDIIIDIDIDIDDIIIIDDDDIIIDIDDIIDDIIDDIDDIIDIIIDDIIDDDIIDIIDIDDIDIDDDDIDIIDIIDDDIIIIIDDIIIDDIIIDDIIIIDDDDDDIIIDIIIIIIDDIDDDIIDIIIDDDDDDIDIIIIIIDIDIDDIIIIIDIIIDIIDIDIDIIDDDIDDDD")
    print(r)