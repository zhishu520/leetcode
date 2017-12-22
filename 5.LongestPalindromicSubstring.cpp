#include <string>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.length() == 1 || s.length() ==0)
            return s;
        int len = s.length();
        int midLeft = 0;
        int midRight = 0;
        int maxLeft,maxRight = 0;

        string result;

        for(int i = 0;i < len; i++)
        {
            midLeft = midRight = i;
            int tmp = 1;
            while( midLeft - tmp>0 && midRight + tmp < len && s[midLeft-tmp] == s[midRight+tmp])
                tmp ++;

            if(midRight - midLeft > maxRight - maxLeft)
            {
                maxRight = midRight;
                maxLeft = midLeft;
            }

            midLeft = i;
            midRight = i + 1;

            tmp = 0;
            while( midLeft - tmp>0 && midRight + tmp < len && s[midLeft-tmp] == s[midRight+tmp])
                tmp ++;

            if(midRight - midLeft > maxRight - maxLeft)
            {
                maxRight = midRight;
                maxLeft = midLeft;
            }
        }

        return string(s, maxLeft, maxRight - maxLeft + 1);
    }
};

