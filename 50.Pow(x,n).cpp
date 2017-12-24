
class Solution {
public:
    double myPow(double x, int n) {

        if(x == 1.0)
            return 1.0;
        else if(x < 0.0f)
            return (n & 1 ? -1 : 1) * myPow(-x, n);

        if(x < 0.0000001)
            return 0;

        if(n < 0)
            return myPow(1/x,-n-1) * 1/x; // 防止溢出


        if(n == 0)
            return 1;
        else if(n == 1)
            return x;
        else if(n & 1)
            return myPow(x*x, n/2) * x;
        else
            return myPow(x*x, n/2);
    }
};

