class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int xx=0;
        for(auto it:nums){
            xx=xx^it;
        }
        int cnt=0;
        int diff=xx^k;
        while(diff){
            if(diff&1)cnt++;
            diff=diff>>1;
        }
        return cnt;
    }
};