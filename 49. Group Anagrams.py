


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = {}

        for i in strs:
            l = list(i)
            l.sort()
            s = "".join(l)

            if dict.has_key(s):
                dict[s].append(i)
            else:
                dict[s] = [i]

        return dict.values()



if __name__ == '__main__':
    s = Solution()
    result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)

