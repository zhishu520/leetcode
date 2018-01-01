class Solution {
public:
    int removeDuplicates(vector<int>& c) {
        c.erase(unique(c.begin(), c.end()), c.end());
        return c.size();
    }
};
