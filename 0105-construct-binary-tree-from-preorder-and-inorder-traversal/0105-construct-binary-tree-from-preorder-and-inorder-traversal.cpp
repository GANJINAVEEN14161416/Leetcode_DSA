/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* construct(vector<int>&Inorder,vector<int>&Preorder,int prein,int preout,int In,int Inout,unordered_map<int,int>&mp){
        if(prein>preout and In>Inout)return NULL;
        TreeNode* root=new TreeNode(Preorder[prein]);
        int numsLeft=mp[root->val]-In;   
        root->left=construct(Inorder,Preorder,prein+1,prein+numsLeft,In,mp[root->val]-1,mp);
        root->right=construct(Inorder,Preorder,prein+numsLeft+1,preout,mp[root->val]+1,Inout,mp);
        return root;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int,int>mp;
        int n=inorder.size();
        for(int i=0;i<n;i++){
            mp[inorder[i]]=i;
        }
        return construct(inorder,preorder,0,preorder.size()-1,0,inorder.size()-1,mp);
        //return root;
    }
};