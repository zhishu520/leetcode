class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        dict = {}

        w = ""
        for i in paragraph:
            if i.isalpha():
                w += i.lower()
            elif w != "":
                if dict.has_key(w):
                    dict[w] += 1
                else:
                    dict.setdefault(w, 1)
                w = ""


        if w != "":
            if dict.has_key(w):
                dict[w] += 1
            else:
                dict.setdefault(w, 1)

        max = 0
        r = ""
        for k, v in dict.items():
            if v > max and banned.count(k) == 0:
                max = v
                r = k

        return r



