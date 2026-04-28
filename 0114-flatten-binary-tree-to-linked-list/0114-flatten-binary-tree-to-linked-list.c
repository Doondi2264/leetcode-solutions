/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void flatten(struct TreeNode* root) {
    if(root==NULL)return;
    flatten(root->left);
    flatten(root->right);

    struct TreeNode* temp;
    temp=root->right;
    root->right=root->left;
    root->left=NULL;

    struct TreeNode* cur=root;
    while(cur->right!=NULL){
        cur=cur->right;
    }
    cur->right=temp;

}