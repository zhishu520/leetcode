#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty())
            return "";
        if(strs.size() == 1)
            return strs[0];
        int index = 0;
        int min_len = strs[0].size();
        for(int i = 0; i< strs.size(); i++) {
            if(strs[i].size()< min_len)
            {
                min_len = strs[i].size();
                index = i;
            }
        }

        int max = 0;
        for(int i = 0;i <min_len;i++){
            for(int j = 0;j < strs.size();j++){
                if(strs[j][i] != strs[index][i]) {
                    return string(strs[index].begin(),strs[index].begin()+ i);
                }
            }
        }
        return "";
    }
};
