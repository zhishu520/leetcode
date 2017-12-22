#include <vector>
using namespace std;

/*
 * len(left_part) == len(right_part)
 * max(left_part) <= min(right_part)
 *
 *
 * 条件1: i + j  = m - i + n - j (or m - i + n - j + 1) [为啥是 + 1]
 *    ==> j = (m + n + 1)/2 - i
 *                                        // 后面的不需要了(重复)
 * 条件2 A[i-1] <= B[j] && B[j-1] <= A[i] && A[i+1] > B[j] && B[j+1] > A[i]
 *
 *
 */

class Solution {
    public:
        double findMedianSortedArrays(vector<int>& A, vector<int>& B) {
            int m = A.size();
            int n = B.size();

            if(m > n)
                return findMedianSortedArrays(B,A);


            int imin = 0,imax = m;
            int half_len = (m + n + 1)/2;
            while(imin <= imax)
            {
                int i = (imin + imax) / 2; // 对二分法不熟悉
                int j = half_len - i;
                if(i > 0 && A[i-1] > B[j]) {
                    imax = i - 1;
                }else if(i < m && B[j-1] > A[i]){ // 对条件不熟悉
                    imin = i + 1;
                }else{
                    int max_left;
                    if(i == 0) max_left = B[j-1];
                    else if(j == 0 ) max_left = A[i-1];
                    else max_left = max(A[i-1], B[j-1]);

                    if((m+n) % 2 == 1)
                        return max_left;
                    int min_right;
                    if(i == m) min_right = B[j];
                    else if(j==n) min_right = A[i];
                    else min_right = min(A[i],B[j]);

                    return (min_right + max_left)/2.0f;
                }
            }

            return 0.0;
        }

};
