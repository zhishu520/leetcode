class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret=[]
        count=1
        for i in range(1,len(S)):
            if(S[i]==S[i-1]):
                count=count+1
            else:
                if(count>2):
                    ret.append([i-count,i-1])
                count=1
        if(count>2):
            ret.append([len(S)-count,len(S)-1])
        return ret