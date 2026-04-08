/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool ismirror(struct TreeNode* a, struct TreeNode* b);

bool isSymmetric(struct TreeNode* root) {
    if (root==NULL)
        return true;
    return ismirror(root->left,root->right);
}

bool ismirror(struct TreeNode* l, struct TreeNode* r){
    if(l==NULL && r==NULL)
        return true;
    if(l==NULL || r==NULL || l->val!=r->val)
        return false;
    return ismirror(l->left,r->right) && ismirror(l->right,r->left);
}