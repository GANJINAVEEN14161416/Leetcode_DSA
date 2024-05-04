class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int l=0;
        int n=people.size();
        int r=n-1;
        int ans=0;
        sort(people.begin(),people.end());
        while(l<r){
            if(people[l]+people[r]<=limit){
                people[l]=-1;
                people[r]=-1;
                l++;
                r--;
                ans++;
            }
            else if(people[l]+people[r]>limit){
                r--;
            }
            else l++;
        }
        for(auto it:people){
            if(it!=-1){
                ans++;
            }
        }
        return ans;
    }
};