#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int a[26] = {0};
        a['I' - 'A'] = 1;
        a['V' - 'A'] = 5;
        a['X' - 'A'] = 10;
        a['L' - 'A'] = 50;
        a['C' - 'A'] = 100;
        a['D' - 'A'] = 500;
        a['M' - 'A'] = 1000;

        int size = s.size();
        int result = 0;
        for(int i = 0;i < size; i++) {
            int index = s[i] - 'A';

            if(i + 1 < size) {
                int nextIndex = s[i+1] - 'A';
                if(a[index] < a[nextIndex]) {
                    result -= a[index];
                    continue;
                }
            }

            result += a[index];
        }
        return result;
    }
};
