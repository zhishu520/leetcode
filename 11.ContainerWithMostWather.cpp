#include <vector>
using namespace std;

class Solution {
 public:
    int maxArea(vector<int>& A) {
        int size = A.size();
        int beg = 0;
        int end = size-1;
        int max_area = 0;
        for(int i = 0;i < size; i++) {
            max_area = max(max_area, min(A[beg],A[end])*(end-beg));
            if(A[beg] > A[end]) {
                end --;
            }else{
                beg++;
            }
        }

        return max_area;
    }
};
