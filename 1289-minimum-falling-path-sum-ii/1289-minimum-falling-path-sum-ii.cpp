class Solution {
public:
    int n;
    int solve(int row,int col,vector<vector<int>>&grid,vector<vector<int>>&dp){
        if(row==n)return 0;
        int l=INT_MAX;
        if(dp[row][col]!=1e9)return dp[row][col];
        for(int newcol=0;newcol<n;newcol++){
            if(newcol!=col){
                l=min(l,solve(row+1,newcol,grid,dp)+grid[row][col]);
            }
        }
        return dp[row][col]=l;
    }
    int minFallingPathSum(vector<vector<int>>& grid) {
        n=grid.size();
        vector<vector<int>>dp(n+1,vector<int>(n+1,1e9));
        if(n==1)return grid[0][0];
        int ans=INT_MAX;
        for(int col=0;col<n;col++){
            ans=min(ans,solve(0,col,grid,dp));
        }
        return ans;
    }
};