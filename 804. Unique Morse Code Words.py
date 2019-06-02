class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        strs = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morseset = set()
        
        for i in words:
            morse = ""
            for c in i:
                morse += strs[ord(c) - ord('a')]

            morseset.add(morse)

        return len(morseset)


if __name__ == "__main__":
    s = Solution()





