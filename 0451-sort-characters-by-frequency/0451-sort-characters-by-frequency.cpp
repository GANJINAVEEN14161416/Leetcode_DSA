class Solution {
public:
    string frequencySort(string s) {
        map<char,int>mp;
        for(int i=0;i<s.size();i++){
            mp[s[i]]++;
        }
        priority_queue<pair<int,char>>pq;
        for(auto i:mp){
            pq.push({i.second,i.first});
        }
        string ans="";
        while(!pq.empty()){
            int size=pq.top().first;
            for(int j=0;j<size;j++){
                ans+=pq.top().second;
            }
            pq.pop();
        }
        return ans;
    }
};