#include <vector>
using namespace std;

#define MAX 1010

class Solution {
    public:
        int array[MAX];
        int findLongestChain(vector<vector<int>>& pairs) {
            for(int i = 0;i <MAX;i++)
                array[i] = 1;


            sort(pairs.begin(),pairs.end(),[this](vector<int>& a,vector<int>& b){
                return a[0] < b[0];
            });

            for(int i = 0; i < pairs.size(); i++)
            {
                for(int j = 0;j < i;j++)
                {
                    if(pairs[i][0] > pairs[j][1] && array[i] < array[j] + 1)
                        array[i] = array[j] + 1;
                }
            }
            int max = 1;
            for(int i = 0;i < MAX;i++)
                if(array[i] > max)
                    max = array[i];


            return max;
        }

};


int main(int argc, char *argv[])
{

    return 0;
}
