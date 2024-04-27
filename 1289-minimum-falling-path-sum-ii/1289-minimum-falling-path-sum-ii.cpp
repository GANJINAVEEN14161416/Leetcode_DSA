class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        int n=grid.size();
        int minValue1=-1;
        int minValue2=-1;
        vector<vector<int>>dp(n+1,vector<int>(n+1,0));
        for(int i=0;i<n;i++){
            dp[n-1][i]=grid[n-1][i];
            if(minValue1==-1 or dp[n-1][i]<=dp[n-1][minValue1]){
                minValue2=minValue1;
                minValue1=i;
            }
            else if(minValue2==-1 or dp[n-1][i]<=dp[n-1][minValue2]){
                minValue2=i;
            }
        }
        for(int row=n-2;row>=0;row--) {
               int temp1=1e9;
                int temp2=1e9;
            for(int col=0;col<n;col++){
                if(minValue1!=col){
                    dp[row][col]=grid[row][col]+dp[row+1][minValue1];
                }
                else if(minValue2!=col){
                    dp[row][col]=grid[row][col]+dp[row+1][minValue2];
                }
                if(temp1==1e9 or dp[row][col]<=dp[row][temp1]){
                    temp2=temp1;
                    temp1=col;
                }
                else if(temp2==1e9 or dp[row][col]<=dp[row][temp2]){
                    temp2=col;
                }
            }
            minValue1=temp1;
            minValue2=temp2;
        }
        
     return dp[0][minValue1];
    }
};