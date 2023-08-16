class Solution {
public:
    int solve(int dp[],int ind){
        if(ind<0)return 0;
        if(ind==0)return dp[ind]=1;
        if(dp[ind]!=-1)return dp[ind];
        dp[ind]=solve(dp,ind-1)+solve(dp,ind-2);
        return dp[ind];
    }
    int climbStairs(int n) {
        int dp[46];
        for(int i=0;i<46;i++)dp[i]=-1;
        solve(dp,n);
        return dp[n];
    }
};