class Solution {
public:
    int findMaxK(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int r=n-1;
        int l=0;
        while(l<r){
            if(nums[l]+nums[r]==0)return nums[r];
            if(nums[r]>abs(nums[l]))r--;
            else l++;
        }
        return -1;
    }
};