class Solution {
public:
    int a[1010];

    int minCostClimbingStairs(vector<int>& cost) {
        memset(a,0,sizeof(a));
        cost.push_back(0);
        int size = cost.size();

        a[0] = cost[0];
        a[1] = cost[1];

        for(int i = 2;i < size; i++){
            a[i] = cost[i] + min(a[i-2], a[i-1]);
        }

        return a[size-1];
    }
};
