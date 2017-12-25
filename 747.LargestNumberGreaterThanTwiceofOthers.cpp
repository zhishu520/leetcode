class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int a, b;
        a = b = -1;
        for(int i = 0;i < nums.size();i++){
            if(nums[i] > nums[a]){
                b = a;
                a = i;
            }else if(nums[i] > nums[b]){
                b = i;
            }
        }

        return nums[b] ? (nums[a] / nums[b] >= 2 ? a : -1) : a;
    }
};
