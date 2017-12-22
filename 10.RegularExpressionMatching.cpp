#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:

    bool isMatchStep(char s,char p){

        if(p == '.')
            return true;
        else if(p == '*')
        {

        }
        else if(s == p)
            return true;

        return false;
    }




    bool isMatch(string s, string p) {
        int pLen = p.length();
        int scnt = 0;
        for(int i =0;i < pLen;i++)
        {
            char m = p[i];
            if(m == '*'){
                char pre = p[i-1];
                int j = 0;
                while(j)
                {

                }

            }else if(m == '.'){
                scnt ++;
                continue;
            }else {
                if(p[i] != s[scnt])
                    return false;
                else
                    scnt ++;
            }
        }

        if(scnt != s.size())
            return false;
        return true;
    }
};

int main()
{
    Solution s;
}
