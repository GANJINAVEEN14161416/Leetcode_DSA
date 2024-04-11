class Solution {
public:
    int dp[101][101];
    bool solve(int ind,int open,string s){
        if(ind<0)return false;
        if(open<0)return false;
        if(ind==s.size()){
            return open==0;
        }
        bool isvalid=false;
        if(dp[ind][open]!=-1)return dp[ind][open];
        if(s[ind]=='('){
            isvalid|=solve(ind+1,open+1,s);
        }
        else if(s[ind]==')'){
            isvalid|=solve(ind+1,open-1,s);
        }
        else{
            isvalid|=solve(ind+1,open+1,s);  //"("
            isvalid|=solve(ind+1,open-1,s);   //")"
            isvalid|=solve(ind+1,open,s);    //""
        }
        return dp[ind][open]=isvalid;
    }
    bool checkValidString(string s) {
        memset(dp,-1,sizeof(dp));
        return solve(0,0,s);
    }
};