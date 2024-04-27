class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n=grid.size();
        vector<vector<int>>dp(n+1,vector<int>(n+1,0));
        for(int i=0;i<n;i++){
            dp[n-1][i]=grid[n-1][i];
        }
        int ans=INT_MAX;
        for(int row=n-2;row>=0;row--){
            for(int col=0;col<n;col++){
                int l=INT_MAX;
                for(int newcol=0;newcol<n;newcol++){
                    if(newcol!=col){
                       l=min(l,grid[row][col]+dp[row+1][newcol]);
                    }
                }
                dp[row][col]=l;
            }
        }   
        // for(int i=0;i<n;i++){
        //     for(int j=0;j<n;j++){
        //         cout<<dp[i][j]<<" ";
        //     }
        //     cout<<endl;
        // }
     for(int i=0;i<n;i++){
         ans=min(ans,dp[0][i]);
     }
        return ans;
    }
};