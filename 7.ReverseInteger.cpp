#include <vector>
#include <iostream>
using namespace std;

class Solution {
    public:
        int reverse(int x) {
            if(x == -2147483648)
                return 0;

            if(x < 0)
                return - reverse(-x);
            if(x == 0) return x;

            vector<int> numVect;
            int tmp = x;
            while(tmp)
            {
                numVect.push_back(tmp%10);
                tmp /= 10;
            }

            vector<int> min = {2,1,4,7,4,8,3,6,4,7};
            if(numVect.size() > min.size())
                return 0;

            for(int i = 0;i<min.size(); i++)
                if(numVect[i] > min[i])
                    return 0;

            int rt = 0;
            for(int i =0 ;i < numVect.size(); i++)
            {
                rt *= 10;
                rt += numVect[i];
            }


            return rt;
        }

};


int main()
{
    Solution s;
    cout << s.reverse(-2147483648);

}
