#include <string>
using namespace std;

class Solution {
public:

    int solution(string s,int beg,int end)
    {
        if(end == beg){
            if(s[beg] == '*')
                return 9;
            else
                return 1;
        }

        else if(end - beg == 1){
            if(s[beg] == '0'){
                return 0;
            }else if(s[beg] == '*' && s[beg+1] == '*'){
                return 81 + 16;
            }else if(s[beg] == '*' && s[end] < '7'){
                return 9 + 2;
            }else if(s[beg] == '*'){
                return 9 + 1;
            }else if(s[end] == '*'){
                return 9;
            }else{
                int num = (s[beg] - '0') * 10 + (s[end] -'0');
                if(num > 26){
                    return 1;
                }else{
                    if(s[end] =='0')
                        return 1;
                    else{
                        return 2;
                    }
                }
            }
        }
        else {
            return solution(s,beg,end - 1)* solution(s,end,end) +
                solution(s,beg,end-2) * solution(s,end-1,end);
        }
    }

    int numDecodings(string s) {

        return 0;
    }
};
