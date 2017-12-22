#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string romanToInt(int n) {
        int c[] = {'M','D','C','L','X','V','I'};
        int a[] = {1000,500,100,50,10,5,1};
        int len = sizeof(a)/sizeof(a[0]);

        string result;
        while(n){
            int i = 0;
            while(n / a[i] == 0) i++;

            if(i%2==0 && n/a[i] == 4){
                result += a[i];
                result += c[i-1];
                int num = n / a[i];
                n -= num * a[i];
            }else if(i + 1 < len && i&1 && n/a[i+1] == 9){
                result += a[i+1];
                result += c[i-1];
                n -= 9 * a[i+1];
            }else{
                int num = n / a[i];
                for(int j = 0;j < num; j++)
                    result+= c[i];
                n -= num * a[i];
            }
        }
        return result;
    }
};
