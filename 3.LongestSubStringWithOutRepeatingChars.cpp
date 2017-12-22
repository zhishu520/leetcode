#include <string>
using namespace std;


class Solution {
public:
    char tempArray[300];

    int lengthOfLongestSubstring(string s) {
        if(s.empty())
            return 0;

        int max = 1;
        int len = s.size();

        for(int i = 0;i < len;i++)
        {
            int tempLen = 1;
            memset(tempArray,0,sizeof(tempArray));
            tempArray[s[i]] = 1;

            for(int j = i + 1;j < len;j++)
            {
                if(tempArray[s[j]] == 0)
                {
                    tempArray[s[j]] = 1;
                    tempLen ++;
                    if(tempLen > max)
                        max = tempLen;
                }
                else
                    break;
            }
        }
        return max;
    }
};
