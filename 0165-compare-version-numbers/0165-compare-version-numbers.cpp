class Solution {
public:
    vector<string>getTokens(string version){
        stringstream ss(version);
        string token="";
        vector<string>v;
        while(getline(ss,token,'.')){
            v.push_back(token);
        }
        return v;
    }
    int compareVersion(string version1, string version2) {
        vector<string>Tokens;
        vector<string>v1=getTokens(version1);
        vector<string>v2=getTokens(version2);
        int i=0;
        int j=0;
        int n=v1.size();
        int m=v2.size();
        while(j<max(n,m)){
            int a=(i<n)?stoi(v1[i]):0;
            int b=(i<m)?stoi(v2[i]):0;
            if(a<b)return -1;
            else if(a>b)return 1;
            i++;j++;
        }
        return 0;
    }
};