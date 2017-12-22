#include <string>
#include <iostream>
using namespace std;


class Solution {
    public:
        string convert(string s, int numRows) {
            if(numRows == 1)
                return s;
            int slen = s.size();
            string rt[numRows];

            int temp = 0;
            bool isAdd = true;
            for(int i = 0;i < slen;i++)
            {
                rt[temp] += s[i];
                if(isAdd)
                {
                    temp ++;
                    if(temp >= numRows - 1)
                        isAdd = false;
                }else{
                    temp --;
                    if(temp <= 0)
                        isAdd = true;
                }

            }

            string ans;
            for(int i = 0;i < numRows;i++)
                ans.insert(ans.end(),rt[i].begin(),rt[i].end());
            return ans;
        }
};

int main()
{
    Solution s;
    cout << s.convert("AB", 1);
    return 0;
}
