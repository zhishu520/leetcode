#include <vector>
using namespace std;

class Solution {
public:
    vector< vector<string> > groupAnagrams(vector<string>& strs) {
        vector<string> s = strs;
        for(int i = 0; i < s.size(); i++)
            sort(s[i].begin(), s[i].end());

        vector< vector<string> > temp;
        vector< vector<string> > result;

        /*
        for(int i = 0; i < s.size(); i++){
            bool bfind = false;
            for(int j = 0;j < temp.size(); j++){
                if(strcmp(s[i].c_str(), temp[j][0].c_str()) == 0){
                    temp[j].push_back(s[i]);
                    result[j].push_back(strs[i]);
                    bfind = true;
                }
            }

            if(!bfind){
                vector<string> ta,tr;
                ta.push_back(s[i]);
                tr.push_back(strs[i]);

                temp.push_back(ta);
                result.push_back(tr);
            }
        }
        */

        return result;
    }
};

