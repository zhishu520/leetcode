#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cstdio>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        std::sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
            if( i == 0 || nums[i] != nums[i-1] ){
                int l = i + 1, r = nums.size() -1 , sum = 0 - nums[i];
                while(l < r){
                    if(nums[l] + nums[r] == sum){
                        result.push_back({nums[i], nums[l], nums[r]});
                        while (l < r && nums[l] == nums[l+1]) l++;
                        while (l < r && nums[r] == nums[r-1]) r--;
                        l++; r--;
                    }else{
                        nums[l] + nums[r] < sum ? l++ : r--;
                    }
                }
            }
        }

        return result;
    }
};


int main(int argc, char *argv[])
{
    Solution s;
    vector<int> arr = {-1, 0, 1, 2, -1, -4};
    auto result = s.threeSum(arr);
    for(auto i : result){
        cout << i[0] << " " << i[1] << " " << i[2] << endl;
    }
    return 0;
}
