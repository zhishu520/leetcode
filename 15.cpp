#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    void doPush(set<vector<int>>& v,int a,int b,int c){
        int temp[] = {a,b,c};
        int minIndex = a<=b?a<=c?0:2:b<=c?1:2;
        int maxIndex = c>=b?c>=a?2:0:b>=a?1:0;
        int midIndex = 3 - minIndex - maxIndex;
        vector<int> one = {temp[minIndex] , temp[midIndex] , temp[maxIndex]};
        if(find(v.begin(),v.end(), one) == v.end())
            v.insert(one);
    }
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> result;
        vector<int> nV;
        vector<int> pV;
        int pA[1000000];
        memset(pA,0,sizeof(pA));
        for(int i = 0;i < nums.size(); i++){
            if(nums[i] >=0 ) {
                pV.push_back(nums[i]);
                pA[nums[i]]++;
            }
            else{
                nV.push_back(nums[i]);
            }
        }

        if(pA[0]>=3) result.insert({0,0,0});

        int size = nV.size();
        for(int i =0;i < size;i++) {
            for(int j=i+1;j<size;j++) {
                int k = -nV[i]-nV[j];
                if(pA[k]) doPush(result,nV[i],nV[j],k);
            }
        }

        int pSize = pV.size();
        for(int i =0;i < size;i++) {
            for(int j=0;j<pSize;j++) {
                int pNeed = 1;
                int k = -nV[i]-pV[j];
                if(k == pV[j]) pNeed++;
                if(k>=0 && pA[k]>=pNeed)
                    doPush(result,nV[i],pV[j],k);
            }
        }

        return vector<vector<int>>(result.begin(),result.end());
    }
};
