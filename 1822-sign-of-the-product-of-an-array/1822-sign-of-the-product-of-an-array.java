class Solution {
    public int arraySign(int[] nums) {
        int answer=0;
        for(int n :nums){
            if (n==0){
                return 0;
            }
            if (n<0){
                answer++;
            }
        }
        return answer%2==0?1:-1;
    }
}