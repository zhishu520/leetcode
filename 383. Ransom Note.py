class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        cnts1 = [0] * 255
        cnts2 = [0] * 255

        for i in ransomNote:
            cnts1[ord(i)] += 1

        for i in magazine:
            cnts2[ord(i)] += 1

        for i in range(255):
            if cnts2[i] < cnts1[i]:
                return False

        return True







        return