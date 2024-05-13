class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        vector<int>nums;
        int n=grid.size();
        int m=grid[0].size();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                nums.push_back(grid[i][j]);
            }
        }
        sort(nums.begin(),nums.end());
        unordered_map<int,int>mp;
        int repeat=-1;
        int miss=-1;
        for(auto it:nums){
            mp[it]++;
            if(mp[it]>1){
                repeat=it;
            }
        }
        n=nums.size();
        for(int i=1;i<=n;i++){
            if(mp.find(i)==mp.end()){
                miss=i;
                break;
            }
        }
        return {repeat,miss};
    }
};