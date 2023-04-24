class Solution {
    public int[] getConcatenation(int[] nums) {
        int size=nums.length;
        int[] list1=new int[2*size];
        for(int i=0;i<nums.length;i++){
            list1[i]=nums[i];
            list1[i+size]=nums[i];
        }
        return list1;
        
        
    }
}