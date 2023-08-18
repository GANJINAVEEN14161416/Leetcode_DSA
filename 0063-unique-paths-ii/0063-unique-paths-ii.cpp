class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m=obstacleGrid.size();
        int n=obstacleGrid[0].size();
        int dp[m][n];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(obstacleGrid[i][j]==1){
                    dp[i][j]=0;
                }
                else if(i==0 and j==0)dp[i][j]=1;
                else{
                    int down=0;
                    int left=0;
                    if(i-1>=0)down=obstacleGrid[i][j]+dp[i-1][j];
                    if(j-1>=0)left=obstacleGrid[i][j]+dp[i][j-1];
                    dp[i][j]=down+left;
                }
            }
        }
        return dp[m-1][n-1];
    }
};