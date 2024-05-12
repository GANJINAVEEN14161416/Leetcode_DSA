class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n=grid.size();
        vector<vector<int>>ans;
        for(int row=0;row<=n-3;row++){
             vector<int>temp;
            for(int col=0;col<=n-3;col++){
                int maxi=-1;
                for(int inrow=row;inrow<row+3;inrow++){
                    for(int incol=col;incol<col+3;incol++){
                        maxi=max(maxi,grid[inrow][incol]);
                    }
                }
                temp.push_back(maxi);
            }
            ans.push_back(temp);
        }
        return ans;
    }
};